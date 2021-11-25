import sys
import os
import json
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QComboBox, QDateEdit, QDialog, QDoubleSpinBox, QTextEdit
from tablegenerater_UI import Ui_TableGenerate
import generater
from datetime import datetime
from win32com.client import Dispatch

date = datetime.now()
year = str(date.year)
month = str(date.month)
day = str(date.day)
now = year + month.rjust(2, '0') + day.rjust(2, '0')
program_file_path = os.path.dirname(os.path.abspath(__file__))

class MyMainForm(QDialog, Ui_TableGenerate):
    def __init__(self, parent=None) -> None:
        super(MyMainForm, self).__init__(parent=parent)
        self.setWindowTitle('Table Generater v1.0')
        self.setupUi(self)
        self.text_property = self.findChildren(QTextEdit)
        self.spin_property = self.findChildren(QDoubleSpinBox)
        self.date_property = self.findChildren(QDateEdit)
        self.combobox_property = self.findChildren(QComboBox)

        last_log_file = 'last_info.json'
        last_log_dict = None
        if os.path.exists(last_log_file):
            last_log_dict = self.load_info()
        
        self.OK_Button.clicked.connect(self.tabel_generate)
        self.toolButton.clicked.connect(self.open_path)
        self.cancel_Button.clicked.connect(sys.exit)
        self.calcButton.clicked.connect(self.calc_sum)

    def save_info(self):

        dic = {}
        for obj in self.text_property:
            dic[obj.objectName()] = obj.toPlainText()
        for obj in self.spin_property:
            dic[obj.objectName()] = obj.value()
        for obj in self.date_property:
            dic[obj.objectName()] = obj.dateTime().toString('yyyy:MM:dd')
        for obj in self.combobox_property:
            dic[obj.objectName()] = obj.currentText()
        dic[self.dir_path.objectName()] = self.dir_path.text()

        if dic['network_department'] == '其他...':
            dic['network_department'] = dic['network_department_other']
            dic.pop('network_department_other')
        
        if dic['start_add'] == '其他...':
            dic['start_add'] = dic['start_add_other']
            dic.pop('start_add_other')

        money = '%.2f' % dic['money']
        dic['money'] = str(money)
        num_list = generater.number_transfer(money)
        money_CN_list = ['money_penny','money_cent', 'money_one', 'money_ten', 'money_h', 'money_t', 'money_tt']
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
        with open('last_info.json') as f:
            info_dict = json.load(f)

        info_dict['network_department_other'] = ''
        info_dict['start_add_other'] = ''
            
        for obj in self.text_property:
            try:
                obj.setPlainText(info_dict[obj.objectName()])
            except KeyError:
                continue
            
        for obj in self.spin_property:
            obj.setValue(float(info_dict[obj.objectName()]))
        for obj in self.combobox_property:
            obj.setCurrentText(info_dict[obj.objectName()])
        self.dir_path.setText(info_dict[self.dir_path.objectName()])

    def trans_doc_pdf(self, doc_filepath, pdf_filepath):

        word = Dispatch('Word.Application')
        doc = word.Documents.Open(doc_filepath)
        doc.SaveAs(pdf_filepath, FileFormat = 17)
        doc.Close()
        word.Quit()

    def generate_filename(self):
        i = 1
        while True:
            filename = now + '_' + str(i)
            if os.path.exists(filename + '.docx'):
                i += 1
            else:
                return filename

    def open_path(self):
        file_dir= QtWidgets.QFileDialog.getExistingDirectory(self, "选择保存位置", os.getcwd())
        self.dir_path.setText(file_dir)
    
    def calc_sum(self):
        l = [self.package.value(),self.agency_fund.value(), self.self_fee.value(), self.transfer_fee.value(), self.delivery_cost.value()]
        sum_value = 0.0
        for i in l:
            i = float(i)
            sum_value += i
        self.money.setValue(sum_value)

    def tabel_generate(self):
        dic = self.save_info()
        filename = self.generate_filename()
        if dic['dir_path']:
            dir_path = dic['dir_path'] + '//'
        else:
            dir_path = program_file_path + '//'

        filename = dir_path + filename
        doc_filepath = filename + '.docx'
        pdf_filepath = filename + '.pdf'
        generater.table_generate(dic, doc_filepath)
        self.trans_doc_pdf(doc_filepath, pdf_filepath)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainForm()
    myWin.show()
    sys.exit(app.exec_())
    
