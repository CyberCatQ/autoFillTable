import json
import os
from datetime import datetime
import pandas as pd

from mailmerge import MailMerge
from docx import Document
from docxcompose.composer import Composer

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QComboBox, QDateEdit, QDialog,
                             QDoubleSpinBox, QLineEdit)

from UI import Ui_TableGenerate

import os
import cv2
from paddleocr import PPStructure, draw_structure_result, save_structure_res

date = datetime.now()
year = str(date.year)
month = str(date.month)
day = str(date.day)
now = year + month.rjust(2, '0') + day.rjust(2, '0')
program_file_path = os.path.dirname(os.path.abspath(__file__))

fields = {'No',              # 红色编号
          'add',             # 送货地址
          'agency_fund',     # 代收款
          'code',            # 单号
          'count',           # 数量
          'date_day',        # 日期：日
          'date_month',      # 日期：月
          'date_year',       # 日期：年
          'delivery_cost',   # 配送费
          'goods_name',      # 品名
          'money',           # 金额(小写)
          'money_cent',      # 大写金额：角
          'money_h',         # 大写金额：佰
          'money_one',       # 大写金额：元
          'money_penny',     # 大写金额：分
          'money_t',         # 大写金额：仟
          'money_ten',       # 大写金额：拾
          'money_tt',        # 大写金额：万
          'network_department',  # 网络单位
          'package',         # 包装
          'payment_method',  # 支付方式
          'people_name',     # 收货人姓名
          'phone_number',    # 电话
          'self_fee',        # 自提费
          'start_add',       # 始发站
          'transfer_fee',    # 中转费
          'weight'}          # 重量

default_dic = {}
for index in fields:
    default_dic[index] = ''

number_dict = {
    '1': '一',
    '2': '二',
    '3': '三',
    '4': '四',
    '5': '五',
    '6': '六',
    '7': '七',
    '8': '八',
    '9': '九',
    '0': '零',
}


def _table_generate(data_dict: dict, file_name=''):
    date = data_dict['dateEdit'].split(':')
    data_dict['date_day'] = date[2]
    data_dict['date_month'] = date[1]
    data_dict['date_year'] = date[0]
    
    for key, value in data_dict.items():
        data_dict[key] = str(value)
        
    default_dic.update(data_dict)
    if not os.path.exists('template.docx'):
        raise FileNotFoundError('No template.docx found.')
        
    template = MailMerge('template.docx')
    template.merge(
        count = default_dic['count'],
        date_month = default_dic['date_month'],
        date_day = default_dic['date_day'],
        money_one = default_dic['money_one'],
        package = default_dic['package_value'],
        transfer_fee = default_dic['transfer_fee_value'],
        start_add = default_dic['start_add'],
        money_h = default_dic['money_h'],
        agency_fund = default_dic['agency_fund_value'],
        delivery_cost = default_dic['delivery_cost_value'],
        code = default_dic['code'],
        payment_method = default_dic['payment_method'],
        network_department = default_dic['network_department'],
        money = default_dic['total_money'],
        goods_name = default_dic['goods_name'],
        money_t = default_dic['money_t'],
        money_penny = default_dic['money_penny'],
        date_year = default_dic['date_year'],
        add = default_dic['add'],
        weight = default_dic['weight'],
        people_name = default_dic['people_name'],
        money_cent = default_dic['money_cent'],
        phone_number = default_dic['phone_number'],
        self_fee = default_dic['self_fee_value'],
        money_tt = default_dic['money_tt'],
        money_ten = default_dic['money_ten'],
        No = default_dic['Code_No']
    )
    template.write(file_name)


def _number_transfer(number: str):
    number = str(number)
    listnum = list(number)
    result = []
    for i in listnum:
        if i == '.':
            continue
        result.append(number_dict[i])

    return result

    
class MyMainForm(QDialog, Ui_TableGenerate):
    def __init__(self, parent=None) -> None:
        super(MyMainForm, self).__init__(parent=parent)
        self.setWindowTitle('Table Generator v1.1')
        self.setupUi(self)
        self.text_property = self.findChildren(QLineEdit)
        self.spin_property = self.findChildren(QDoubleSpinBox)
        self.date_property = self.findChildren(QDateEdit)
        self.combobox_property = self.findChildren(QComboBox)

        self.output_dir = os.getcwd()
        self.filename = now + '_' + '1'
        self.Code_No.setText('1'.rjust(9, '0'))

        self.file_to_merge = []
        self.img_path = ''

        self.last_log_file = program_file_path + os.sep + 'last_info.json'
        if os.path.exists(self.last_log_file):
            self.load_info()
        
        self.OK_Button.clicked.connect(self.tabel_generate)
        self.toolButton.clicked.connect(self.open_path)
        self.calcButton.clicked.connect(self.calc_sum)
        self.pushButton_addmerge.clicked.connect(self.add_exist_file)
        self.pushButton_merge.clicked.connect(self.merge_files_in_list)

    @property
    def docx_filepath(self):
        return self.output_dir + '/' + self.filename + '.docx'

    def _get_file(self):
        return QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', os.getcwd())

    def save_info(self):

        dic = {}
        for obj in self.text_property:
            dic[obj.objectName()] = obj.text()
        for obj in self.spin_property:
            dic[obj.objectName()] = obj.value()
        for obj in self.date_property:
            dic[obj.objectName()] = obj.dateTime().toString('yyyy:MM:dd')
        for obj in self.combobox_property:
            dic[obj.objectName()] = obj.currentText()
        dic[self.dir_path.objectName()] = self.dir_path.text()

        dic['count'] = int(dic['count'])

        if dic['network_department'] == '其他...':
            dic['network_department'] = dic['network_department_other']
            dic.pop('network_department_other')
        
        if dic['start_add'] == '其他...':
            dic['start_add'] = dic['start_add_other']
            dic.pop('start_add_other')

        money = '%.2f' % dic['total_money']
        dic['total_money'] = str(money)
        num_list = _number_transfer(money)
        money_CN_list = ['money_penny','money_cent', 'money_one', 'money_ten', 'money_h', 'money_t', 'money_tt']
        for key in money_CN_list:
            dic[key] = ''

        i = -1
        for t in money_CN_list:
            try:
                dic[t] = num_list[i]
                i -= 1
            except IndexError:
                break

        with open('last_info.json', 'w') as f:
            f.write(json.dumps(dic))

        return dic

    def load_info(self):
        with open(self.last_log_file) as f:
            info_dict = json.load(f)

        info_dict['network_department_other'] = ''
        info_dict['start_add_other'] = ''
            
        for obj in self.text_property:
            try:
                obj.setText(info_dict[obj.objectName()])
            except KeyError:
                continue
        if not info_dict['Code_No']:
            info_dict['Code_No'] = '0'
        self.Code_No.setText(str(int(info_dict['Code_No']) + 1).rjust(9, '0'))
            
        for obj in self.spin_property:
            obj.setValue(float(info_dict[obj.objectName()]))
        for obj in self.combobox_property:
            obj.setCurrentText(info_dict[obj.objectName()])
        self.dir_path.setText(info_dict[self.dir_path.objectName()])

    def generate_filename(self):
        i = 1
        while True:
            self.filename = now + '_' + str(i)
            if os.path.exists(self.docx_filepath):
                i += 1
            else:
                break

    def open_path(self):
        file_dir= QtWidgets.QFileDialog.getExistingDirectory(self, "选择保存位置", os.getcwd())
        if file_dir:
            self.dir_path.setText(file_dir)
    
    def calc_sum(self):
        l = [self.package_value.value(),self.agency_fund_value.value(), self.self_fee_value.value(), self.transfer_fee_value.value(), self.delivery_cost_value.value()]
        sum_value = 0.0
        for i in l:
            i = float(i)
            sum_value += i
        self.total_money.setValue(sum_value)
    
    def add_to_merge(self, file_path):
        self.listWidget.addItem(file_path)
        self.file_to_merge.append(file_path)
    
    def add_exist_file(self):
        file_path = self._get_file()
        if file_path[0]:
            self.add_to_merge(file_path[0])

    def merge_files_in_list(self):
        result_file = self.dir_path.text() + '/' + now + '_总.docx'
        
        if not self.file_to_merge:
            return
        else:
            merged_docx = Document(self.file_to_merge[0])
            composer = Composer(merged_docx)
            for i in self.file_to_merge[1:]:
                composer.append(Document(i))

            composer.save(result_file)
            self.status_label.setText("表单文件 %s 已生成" % result_file)

    def tabel_generate(self):
        dic = self.save_info()
        if dic['dir_path']:
            self.output_dir = dic['dir_path']
        else:
            self.output_dir = os.getcwd()
        self.generate_filename()
        _table_generate(dic, self.docx_filepath)
        self.status_label.setText("表单文件 %s 已生成" % self.docx_filepath)
        self.add_to_merge(os.path.abspath(self.docx_filepath))

        current_No = self.Code_No.text() if self.Code_No.text() else '0'
        self.Code_No.setText(str(int(current_No) + 1).rjust(9, '0'))
    
    def get_img_excel_path(self):
        pass

class OCR:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_type = self._check_type()
        self.data = None

    def _check_type(self):
        suffix = self.file_path.split('.')[-1]
        support_img_type = ['jpg', 'jpeg', 'png', 'bmp']
        for i in support_img_type:
            if i == suffix:
                return 'img'

        if self.file_path.endswith('.xlsx') or self.file_path.endswith('.xls'):
            return 'excel'
        
        raise TypeError('不支持的文件类型')

    def ocr(self):
        table_engine = PPStructure(show_log=False)
        #save_folder = self.dir_path.text() + '/excel'
        img_path = self.file_path
        img = cv2.imread(img_path)
        result = table_engine(img)
        #save_structure_res(result, save_folder, os.path.basename(img_path).split('.')[0])
        self.data = pd.read_html(result[0]['res'][1])
        