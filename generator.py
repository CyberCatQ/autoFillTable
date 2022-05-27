import json
import os

from docx import Document
from docxcompose.composer import Composer
from mailmerge import MailMerge
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import (QComboBox, QDateEdit, QDialog, QDoubleSpinBox,
                             QLineEdit, QTableWidgetItem)

from _config import fields, __version__, now, program_file_path, number_dict, ShunJieCfg
from _ocr import OCR
from _UI import Ui_TableGenerate

default_dic = {k : '' for k in fields}

class QSSLoader:
    def __init__(self, file_path='style.qss') -> None:
        self.file_path = file_path
    
    @staticmethod
    def read_qss_file(file_path):
        with open(file_path, 'r') as f:
            return f.read()
    
    def get_style_sheet(self):
        return self.read_qss_file(self.file_path)

class MyMainForm(QDialog, Ui_TableGenerate):
    def __init__(self, parent=None) -> None:
        super(MyMainForm, self).__init__(parent=parent)
        self.setWindowTitle(f'Table Generator v{__version__}')
        self.setupUi(self)
        self.beautify()
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.ocr_info_table.setColumnCount(4)
        self.ocr_info_table.setHorizontalHeaderLabels(['收件人', '件数', '重量', '代收款'])
        font = self.ocr_info_table.horizontalHeader().font()
        font.setBold(True)
        self.ocr_info_table.horizontalHeader().setFont(font)
        self.ocr_info_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.text_property = self.findChildren(QLineEdit)
        self.spin_property = self.findChildren(QDoubleSpinBox)
        self.date_property = self.findChildren(QDateEdit)
        self.combobox_property = self.findChildren(QComboBox)

        self.output_file = f'{now}_1.docx'

        self._startPos = None
        self. _endPos = None
        self._isTracking = None

        self.file_to_merge = []
        self.img_path = ''
        self.last_log_file = os.path.join(program_file_path, 'last_log.json')
        if os.path.exists(self.last_log_file):
            self.load_info(self.last_log_file)

        self.minimizeButton.clicked.connect(self.showMinimized)
        self.closeButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.OK_Button.clicked.connect(self.table_generate)
        self.toolButton.clicked.connect(self.get_dir_path)
        self.calcButton.clicked.connect(self.calc_sum)
        self.pushButton_addmerge.clicked.connect(self.add_exist_file)
        self.pushButton_merge.clicked.connect(self.merge_files_in_list)
        self.pushButton_ocr.clicked.connect(self.run_ocr)
        self.ocr_button.clicked.connect(self.table_generate_from_ocr)

    def beautify(self):
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        
    # 鼠标移动事件
    def mouseMoveEvent(self, a0: QtGui.QMouseEvent):
        if self._startPos:
            self._endPos = a0.pos() - self._startPos
            # 移动窗口
            self.move(self.pos() + self._endPos)
    
    # 鼠标按下事件
    def mousePressEvent(self, a0: QtGui.QMouseEvent):
        # 根据鼠标按下时的位置判断是否在QFrame范围内
        if self.childAt(a0.pos().x(),a0.pos().y()).objectName() == "frame":
            # 判断鼠标按下的是左键
            if a0.button() == QtCore.Qt.LeftButton:
                self._isTracking = True
                # 记录初始位置
                self._startPos = QtCore.QPoint(a0.x(), a0.y())

    # 鼠标松开事件
    def mouseReleaseEvent(self, a0: QtGui.QMouseEvent):
        if a0.button() == QtCore.Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    @property
    def output_dir(self):
        return self.dir_path.text() or os.getcwd()

    @property
    def docx_filepath(self):
        return os.path.join(self.output_dir, self.output_file)

    @staticmethod
    def _number_transfer(number: str):
        number = str(number)
        number_splits = number.split('.')
        number_int = number_splits[0]
        number_dec = number_splits[1].ljust(2, '0')
        int_dict = ['money_one', 'money_ten', 'money_h', 'money_t', 'money_tt']
        dec_dict = ['money_dime', 'money_cent']
        result = {k: '' for k in [*int_dict, *dec_dict]}

        for index, num in enumerate(number_int[::-1]):
            result[int_dict[index]] = number_dict[num]
        for index, num in enumerate(number_dec):
            result[dec_dict[index]] = number_dict[num]
        return result

    def _get_file(self):
        return QtWidgets.QFileDialog.getOpenFileName(self, '选择文件', os.getcwd())

    def save_info(self):
        # 保存UI数据到文件
        dic = {}
        for obj in self.text_property:
            dic[obj.objectName()] = obj.text()
        for obj in self.spin_property:
            dic[obj.objectName()] = obj.value()
        for obj in self.date_property:
            dic[obj.objectName()] = obj.dateTime().toString('yyyy:MM:dd')
        for obj in self.combobox_property:
            dic[obj.objectName()] = obj.currentText()
        dic['count'] = int(dic['count'])
        dic['Code_No'] = dic['Code_No'].rjust(9, '0') if dic['Code_No'] else '1'.rjust(9, '0')
        money = str('%.2f' % dic['total_money'])
        dic['total_money'] = str(money)

        if not dic['Code_No']:
            dic['Code_No'] = '1'.rjust(9, '0')

        if dic['network_department'] == '其他...':
            dic['network_department'] = dic['network_department_other']
            dic.pop('network_department_other')
        
        if dic['start_add'] == '其他...':
            dic['start_add'] = dic['start_add_other']
            dic.pop('start_add_other')

        num_transfered_dict = self._number_transfer(money)
        money_CN_list = ['money_dime','money_cent', 'money_one', 'money_ten', 'money_h', 'money_t', 'money_tt']
        for key in money_CN_list:
            dic[key] = ''
        dic.update(num_transfered_dict)

        with open(self.last_log_file, 'w') as f:
            f.write(json.dumps(dic))

    def load_info(self, file_path):
        # load数据到UI
        with open(file_path) as f:
            info_dict = json.load(f)

        info_dict['network_department_other'] = ''
        info_dict['start_add_other'] = ''
        info_dict['Code_No'] = info_dict['Code_No'] if info_dict['Code_No'] else '1'.rjust(9, '0')

        for obj in self.text_property:
            try:
                obj.setText(info_dict[obj.objectName()])
            except KeyError:
                continue
        for obj in self.spin_property:
            obj.setValue(float(info_dict[obj.objectName()]))
        for obj in self.combobox_property:
            obj.setCurrentText(info_dict[obj.objectName()])
    
    def _get_output_file_name(self):
        i = 1
        while True:
            filename = f'{now}_{i}.docx'
            if os.path.exists(os.path.join(self.output_dir, filename)):
                i += 1
            else:
                self.output_file = filename
                return filename

    def read_info(self, file_path):
        # 从json文件读取数据
        with open(file_path) as f:
            info_dict = json.load(f)
        return info_dict

    def get_dir_path(self):
        file_dir= QtWidgets.QFileDialog.getExistingDirectory(self, "选择保存位置", os.getcwd())
        if file_dir:
            self.dir_path.setText(file_dir)
    
    def calc_sum(self):
        _total = [
            self.package_value.value(), 
            self.agency_fund_value.value(), 
            self.self_fee_value.value(), 
            self.transfer_fee_value.value(), 
            self.delivery_cost_value.value()
            ]
        sum_value = sum(map(lambda x: x if x else 0.0, _total))
        self.total_money.setValue(sum_value)
    
    # DOC合并部分
    def add_to_merge(self, file_path):
        self.listWidget.addItem(file_path)
        self.file_to_merge.append(file_path)
    
    def add_exist_file(self):
        file_path = self._get_file()
        if file_path[0]:
            self.add_to_merge(file_path[0])

    def merge_files_in_list(self):
        result_file = os.path.join(self.output_dir, f'{now}_总.docx')
        if not self.file_to_merge:
            return
        else:
            merged_docx = Document(self.file_to_merge[0])
            composer = Composer(merged_docx)
            for i in self.file_to_merge[1:]:
                composer.append(Document(i))
            composer.save(result_file)
            self.status_label.setText("表单文件 %s 已生成" % result_file)

    # 单个表格文件生成部分
    def _table_generate(self, data_dict: dict, output_file_path=None):
        date = data_dict['dateEdit'].split(':')
        data_dict['date_year'], data_dict['date_month'], data_dict['date_day'] = date
        data_dict = {k : str(v) for k, v in data_dict.items()}
        default_dic.update(data_dict)

        if not os.path.exists('template.docx'):
            raise FileNotFoundError('template.docx is not found.')
            
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
            money_dime = default_dic['money_dime'],
            date_year = default_dic['date_year'],
            add = default_dic['add'],
            weight = default_dic['weight'],
            people_name = default_dic['people_name'],
            money_cent = default_dic['money_cent'],
            phone_number = default_dic['phone_number'],
            self_fee = default_dic['self_fee_value'],
            money_tt = default_dic['money_tt'],
            money_ten = default_dic['money_ten'],
            Code_No = default_dic['Code_No']
        )
        template.write(output_file_path)

    def table_generate(self):
        self.save_info()
        data_dict = self.read_info(self.last_log_file)
        self.output_file = self._get_output_file_name()

        self._table_generate(data_dict, self.docx_filepath)
        self.status_label.setText(f"表单文件{self.docx_filepath}已生成")
        self.add_to_merge(os.path.abspath(self.docx_filepath))

        # 序号自动增加
        current_No = self.Code_No.text() if self.Code_No.text() else '1'
        self.Code_No.setText(str(int(current_No) + 1).rjust(9, '0'))
    
    def get_ocr_cfg(self, network_department):
        if network_department == '顺捷':
            return ShunJieCfg()

    def run_ocr(self):
        file_path = self._get_file()
        if file_path[0]:
            self.ocr_info_table.clearContents()
            ocr_department = self.ocr_network.currentText()
            cfg = self.get_ocr_cfg(ocr_department)

            ocr = OCR(file_path[0], cfg)
            ocr_data = ocr.ocr()
            for item in ocr_data:
                row = self.ocr_info_table.rowCount()
                self.ocr_info_table.insertRow(row)
                for i, value in enumerate(item.values()):
                    self.ocr_info_table.setItem(row, i, QTableWidgetItem(value))
                
    def read_ocr(self):
        ocr_data = []
        for row_index in range(self.ocr_info_table.rowCount()):
            row_data = {}
            row_data['people_name'] = self.ocr_info_table.item(row_index, 0).text()
            row_data['count'] = self.ocr_info_table.item(row_index, 1).text()
            row_data['weight'] = self.ocr_info_table.item(row_index, 2).text()
            row_data['agency_fund_value'] = self.ocr_info_table.item(row_index, 3).text()
            row_data['total_money'] = row_data['agency_fund_value']
            ocr_data.append(row_data)

        return ocr_data
    
    def table_generate_from_ocr(self):
        final_ocr_data = self.read_ocr()
        department = self.ocr_network.currentText()
        ADD = self.get_ocr_cfg(department).ADDRESS

        for index, data_dict in enumerate(final_ocr_data):
            self.people_name.setText(data_dict['people_name'])
            self.network_department.setCurrentText(department)
            self.start_add.setCurrentText(ADD)
            self.count.setValue(float(data_dict['count']))
            self.weight.setValue(float(data_dict['weight']))
            self.agency_fund_value.setValue(float(data_dict['agency_fund_value']))
            self.total_money.setValue(float(data_dict['total_money']))
            self.save_info()
            self.output_file = self._get_output_file_name()
            self.table_generate()
