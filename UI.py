# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TableGenerate(object):
    def setupUi(self, TableGenerate):
        TableGenerate.setObjectName("TableGenerate")
        TableGenerate.resize(763, 629)
        TableGenerate.setMinimumSize(QtCore.QSize(763, 629))
        TableGenerate.setMaximumSize(QtCore.QSize(763, 629))
        self.toolButton = QtWidgets.QToolButton(TableGenerate)
        self.toolButton.setGeometry(QtCore.QRect(480, 570, 51, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.toolButton.setFont(font)
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolButton.setObjectName("toolButton")
        self.label_20 = QtWidgets.QLabel(TableGenerate)
        self.label_20.setGeometry(QtCore.QRect(24, 570, 101, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.dir_path = QtWidgets.QLineEdit(TableGenerate)
        self.dir_path.setGeometry(QtCore.QRect(134, 570, 341, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.dir_path.setFont(font)
        self.dir_path.setObjectName("dir_path")
        self.status_label = QtWidgets.QLabel(TableGenerate)
        self.status_label.setGeometry(QtCore.QRect(30, 530, 701, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.status_label.setFont(font)
        self.status_label.setText("")
        self.status_label.setObjectName("status_label")
        self.tabWidget = QtWidgets.QTabWidget(TableGenerate)
        self.tabWidget.setGeometry(QtCore.QRect(10, 20, 751, 601))
        self.tabWidget.setMaximumSize(QtCore.QSize(751, 601))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.input_tab = QtWidgets.QWidget()
        self.input_tab.setObjectName("input_tab")
        self.agency_fund_label = QtWidgets.QLabel(self.input_tab)
        self.agency_fund_label.setGeometry(QtCore.QRect(370, 210, 95, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.agency_fund_label.setFont(font)
        self.agency_fund_label.setObjectName("agency_fund_label")
        self.label_19 = QtWidgets.QLabel(self.input_tab)
        self.label_19.setGeometry(QtCore.QRect(700, 70, 54, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.dateEdit = QtWidgets.QDateEdit(self.input_tab)
        self.dateEdit.setGeometry(QtCore.QRect(110, 10, 231, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.dateEdit.setFont(font)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setObjectName("dateEdit")
        self.package_value = QtWidgets.QDoubleSpinBox(self.input_tab)
        self.package_value.setGeometry(QtCore.QRect(460, 170, 91, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.package_value.setFont(font)
        self.package_value.setMaximum(999999.99)
        self.package_value.setObjectName("package_value")
        self.start_add = QtWidgets.QComboBox(self.input_tab)
        self.start_add.setGeometry(QtCore.QRect(110, 190, 121, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.start_add.setFont(font)
        self.start_add.setObjectName("start_add")
        self.start_add.addItem("")
        self.start_add.addItem("")
        self.start_add.addItem("")
        self.start_add.addItem("")
        self.start_add.addItem("")
        self.start_add.addItem("")
        self.start_add.addItem("")
        self.start_add.addItem("")
        self.start_add.addItem("")
        self.start_add.addItem("")
        self.start_add.addItem("")
        self.start_add.addItem("")
        self.start_add.addItem("")
        self.label_18 = QtWidgets.QLabel(self.input_tab)
        self.label_18.setGeometry(QtCore.QRect(560, 70, 54, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.package_label = QtWidgets.QLabel(self.input_tab)
        self.package_label.setGeometry(QtCore.QRect(370, 170, 95, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.package_label.setFont(font)
        self.package_label.setObjectName("package_label")
        self.label_7 = QtWidgets.QLabel(self.input_tab)
        self.label_7.setGeometry(QtCore.QRect(20, 370, 54, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.total_money = QtWidgets.QDoubleSpinBox(self.input_tab)
        self.total_money.setGeometry(QtCore.QRect(460, 440, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.total_money.setFont(font)
        self.total_money.setMaximum(999999.99)
        self.total_money.setObjectName("total_money")
        self.label_6 = QtWidgets.QLabel(self.input_tab)
        self.label_6.setGeometry(QtCore.QRect(20, 310, 80, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_3 = QtWidgets.QLabel(self.input_tab)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 80, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.self_fee_value = QtWidgets.QDoubleSpinBox(self.input_tab)
        self.self_fee_value.setGeometry(QtCore.QRect(460, 290, 91, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.self_fee_value.setFont(font)
        self.self_fee_value.setMaximum(999999.99)
        self.self_fee_value.setObjectName("self_fee_value")
        self.network_department = QtWidgets.QComboBox(self.input_tab)
        self.network_department.setGeometry(QtCore.QRect(110, 130, 121, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.network_department.setFont(font)
        self.network_department.setEditable(False)
        self.network_department.setObjectName("network_department")
        self.network_department.addItem("")
        self.network_department.addItem("")
        self.network_department.addItem("")
        self.network_department.addItem("")
        self.network_department.addItem("")
        self.network_department.addItem("")
        self.network_department.addItem("")
        self.network_department.addItem("")
        self.network_department.addItem("")
        self.network_department.addItem("")
        self.network_department.addItem("")
        self.network_department.addItem("")
        self.network_department.addItem("")
        self.network_department.addItem("")
        self.network_department.addItem("")
        self.network_department.addItem("")
        self.network_department.addItem("")
        self.network_department.addItem("")
        self.label_17 = QtWidgets.QLabel(self.input_tab)
        self.label_17.setGeometry(QtCore.QRect(20, 430, 54, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.transfer_fee_value = QtWidgets.QDoubleSpinBox(self.input_tab)
        self.transfer_fee_value.setGeometry(QtCore.QRect(460, 330, 91, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.transfer_fee_value.setFont(font)
        self.transfer_fee_value.setMaximum(999999.99)
        self.transfer_fee_value.setObjectName("transfer_fee_value")
        self.weight = QtWidgets.QDoubleSpinBox(self.input_tab)
        self.weight.setGeometry(QtCore.QRect(590, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.weight.setFont(font)
        self.weight.setDecimals(1)
        self.weight.setMaximum(999999.0)
        self.weight.setObjectName("weight")
        self.count = QtWidgets.QDoubleSpinBox(self.input_tab)
        self.count.setGeometry(QtCore.QRect(460, 70, 91, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.count.setFont(font)
        self.count.setDecimals(0)
        self.count.setMaximum(999999.0)
        self.count.setObjectName("count")
        self.label_8 = QtWidgets.QLabel(self.input_tab)
        self.label_8.setGeometry(QtCore.QRect(370, 10, 95, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.transfer_fee_label = QtWidgets.QLabel(self.input_tab)
        self.transfer_fee_label.setGeometry(QtCore.QRect(370, 330, 95, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.transfer_fee_label.setFont(font)
        self.transfer_fee_label.setObjectName("transfer_fee_label")
        self.total_money_label = QtWidgets.QLabel(self.input_tab)
        self.total_money_label.setGeometry(QtCore.QRect(370, 440, 95, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.total_money_label.setFont(font)
        self.total_money_label.setObjectName("total_money_label")
        self.label = QtWidgets.QLabel(self.input_tab)
        self.label.setGeometry(QtCore.QRect(20, 10, 80, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.agency_fund_value = QtWidgets.QDoubleSpinBox(self.input_tab)
        self.agency_fund_value.setGeometry(QtCore.QRect(460, 210, 91, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.agency_fund_value.setFont(font)
        self.agency_fund_value.setMaximum(999999.99)
        self.agency_fund_value.setObjectName("agency_fund_value")
        self.self_fee_label = QtWidgets.QLabel(self.input_tab)
        self.self_fee_label.setGeometry(QtCore.QRect(370, 290, 95, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.self_fee_label.setFont(font)
        self.self_fee_label.setObjectName("self_fee_label")
        self.label_4 = QtWidgets.QLabel(self.input_tab)
        self.label_4.setGeometry(QtCore.QRect(20, 190, 80, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.delivery_cost_label = QtWidgets.QLabel(self.input_tab)
        self.delivery_cost_label.setGeometry(QtCore.QRect(370, 250, 95, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.delivery_cost_label.setFont(font)
        self.delivery_cost_label.setObjectName("delivery_cost_label")
        self.Code_No = QtWidgets.QLineEdit(self.input_tab)
        self.Code_No.setGeometry(QtCore.QRect(110, 70, 231, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.Code_No.setFont(font)
        self.Code_No.setMaxLength(9999999)
        self.Code_No.setObjectName("Code_No")
        self.delivery_cost_value = QtWidgets.QDoubleSpinBox(self.input_tab)
        self.delivery_cost_value.setGeometry(QtCore.QRect(460, 250, 91, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.delivery_cost_value.setFont(font)
        self.delivery_cost_value.setMaximum(999999.99)
        self.delivery_cost_value.setObjectName("delivery_cost_value")
        self.label_9 = QtWidgets.QLabel(self.input_tab)
        self.label_9.setGeometry(QtCore.QRect(355, 70, 100, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_5 = QtWidgets.QLabel(self.input_tab)
        self.label_5.setGeometry(QtCore.QRect(20, 250, 54, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.payment_method_label = QtWidgets.QLabel(self.input_tab)
        self.payment_method_label.setGeometry(QtCore.QRect(370, 380, 95, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.payment_method_label.setFont(font)
        self.payment_method_label.setObjectName("payment_method_label")
        self.label_2 = QtWidgets.QLabel(self.input_tab)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 54, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.calcButton = QtWidgets.QPushButton(self.input_tab)
        self.calcButton.setGeometry(QtCore.QRect(580, 440, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.calcButton.setFont(font)
        self.calcButton.setObjectName("calcButton")
        self.OK_Button = QtWidgets.QPushButton(self.input_tab)
        self.OK_Button.setGeometry(QtCore.QRect(550, 523, 141, 32))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.OK_Button.setFont(font)
        self.OK_Button.setObjectName("OK_Button")
        self.network_department_other = QtWidgets.QLineEdit(self.input_tab)
        self.network_department_other.setGeometry(QtCore.QRect(250, 130, 91, 31))
        self.network_department_other.setObjectName("network_department_other")
        self.start_add_other = QtWidgets.QLineEdit(self.input_tab)
        self.start_add_other.setGeometry(QtCore.QRect(250, 190, 91, 31))
        self.start_add_other.setObjectName("start_add_other")
        self.code = QtWidgets.QLineEdit(self.input_tab)
        self.code.setGeometry(QtCore.QRect(110, 250, 231, 31))
        self.code.setObjectName("code")
        self.people_name = QtWidgets.QLineEdit(self.input_tab)
        self.people_name.setGeometry(QtCore.QRect(110, 310, 231, 31))
        self.people_name.setObjectName("people_name")
        self.add = QtWidgets.QLineEdit(self.input_tab)
        self.add.setGeometry(QtCore.QRect(110, 370, 231, 31))
        self.add.setObjectName("add")
        self.phone_number = QtWidgets.QLineEdit(self.input_tab)
        self.phone_number.setGeometry(QtCore.QRect(110, 430, 231, 31))
        self.phone_number.setObjectName("phone_number")
        self.goods_name = QtWidgets.QLineEdit(self.input_tab)
        self.goods_name.setGeometry(QtCore.QRect(460, 10, 231, 31))
        self.goods_name.setObjectName("goods_name")
        self.payment_method = QtWidgets.QLineEdit(self.input_tab)
        self.payment_method.setGeometry(QtCore.QRect(460, 380, 231, 31))
        self.payment_method.setObjectName("payment_method")
        self.tabWidget.addTab(self.input_tab, "")
        self.ocr_tab = QtWidgets.QWidget()
        self.ocr_tab.setObjectName("ocr_tab")
        self.pushButton_ocr = QtWidgets.QPushButton(self.ocr_tab)
        self.pushButton_ocr.setGeometry(QtCore.QRect(590, 10, 131, 31))
        self.pushButton_ocr.setObjectName("pushButton_ocr")
        self.ocr_network = QtWidgets.QComboBox(self.ocr_tab)
        self.ocr_network.setGeometry(QtCore.QRect(440, 10, 121, 31))
        self.ocr_network.setObjectName("ocr_network")
        self.ocr_network.addItem("")
        self.ocr_network.setItemText(0, "")
        self.ocr_network.addItem("")
        self.ocr_network.addItem("")
        self.ocr_network.addItem("")
        self.orc_network_label = QtWidgets.QLabel(self.ocr_tab)
        self.orc_network_label.setGeometry(QtCore.QRect(360, 10, 81, 31))
        self.orc_network_label.setObjectName("orc_network_label")
        self.ocr_info_table = QtWidgets.QTableWidget(self.ocr_tab)
        self.ocr_info_table.setGeometry(QtCore.QRect(20, 50, 701, 421))
        self.ocr_info_table.setObjectName("ocr_info_table")
        self.ocr_info_table.setColumnCount(0)
        self.ocr_info_table.setRowCount(0)
        self.ocr_label = QtWidgets.QLabel(self.ocr_tab)
        self.ocr_label.setGeometry(QtCore.QRect(20, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.ocr_label.setFont(font)
        self.ocr_label.setTextFormat(QtCore.Qt.AutoText)
        self.ocr_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.ocr_label.setObjectName("ocr_label")
        self.ocr_button = QtWidgets.QPushButton(self.ocr_tab)
        self.ocr_button.setGeometry(QtCore.QRect(590, 523, 131, 32))
        self.ocr_button.setObjectName("ocr_button")
        self.tabWidget.addTab(self.ocr_tab, "")
        self.merge_tab = QtWidgets.QWidget()
        self.merge_tab.setObjectName("merge_tab")
        self.listWidget = QtWidgets.QListWidget(self.merge_tab)
        self.listWidget.setGeometry(QtCore.QRect(20, 50, 701, 421))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.listWidget.setObjectName("listWidget")
        self.label_merge = QtWidgets.QLabel(self.merge_tab)
        self.label_merge.setGeometry(QtCore.QRect(20, 10, 91, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.label_merge.setFont(font)
        self.label_merge.setTextFormat(QtCore.Qt.AutoText)
        self.label_merge.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_merge.setObjectName("label_merge")
        self.pushButton_addmerge = QtWidgets.QPushButton(self.merge_tab)
        self.pushButton_addmerge.setGeometry(QtCore.QRect(590, 10, 131, 31))
        self.pushButton_addmerge.setObjectName("pushButton_addmerge")
        self.pushButton_merge = QtWidgets.QPushButton(self.merge_tab)
        self.pushButton_merge.setGeometry(QtCore.QRect(590, 523, 131, 32))
        self.pushButton_merge.setObjectName("pushButton_merge")
        self.tabWidget.addTab(self.merge_tab, "")
        self.tabWidget.raise_()
        self.toolButton.raise_()
        self.label_20.raise_()
        self.dir_path.raise_()
        self.status_label.raise_()

        self.retranslateUi(TableGenerate)
        self.tabWidget.setCurrentIndex(1)
        self.network_department.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TableGenerate)
        TableGenerate.setTabOrder(self.dateEdit, self.network_department)
        TableGenerate.setTabOrder(self.network_department, self.start_add)
        TableGenerate.setTabOrder(self.start_add, self.count)
        TableGenerate.setTabOrder(self.count, self.weight)
        TableGenerate.setTabOrder(self.weight, self.package_value)
        TableGenerate.setTabOrder(self.package_value, self.agency_fund_value)
        TableGenerate.setTabOrder(self.agency_fund_value, self.delivery_cost_value)
        TableGenerate.setTabOrder(self.delivery_cost_value, self.self_fee_value)
        TableGenerate.setTabOrder(self.self_fee_value, self.transfer_fee_value)
        TableGenerate.setTabOrder(self.transfer_fee_value, self.total_money)
        TableGenerate.setTabOrder(self.total_money, self.toolButton)
        TableGenerate.setTabOrder(self.toolButton, self.OK_Button)

    def retranslateUi(self, TableGenerate):
        _translate = QtCore.QCoreApplication.translate
        TableGenerate.setWindowTitle(_translate("TableGenerate", "Table Generator"))
        self.toolButton.setText(_translate("TableGenerate", "..."))
        self.label_20.setText(_translate("TableGenerate", "文件保存位置"))
        self.agency_fund_label.setText(_translate("TableGenerate", "代收款"))
        self.label_19.setText(_translate("TableGenerate", "KG"))
        self.dateEdit.setDisplayFormat(_translate("TableGenerate", "yyyy-MM-dd"))
        self.start_add.setItemText(0, _translate("TableGenerate", "武汉"))
        self.start_add.setItemText(1, _translate("TableGenerate", "重庆"))
        self.start_add.setItemText(2, _translate("TableGenerate", "杭州"))
        self.start_add.setItemText(3, _translate("TableGenerate", "天津"))
        self.start_add.setItemText(4, _translate("TableGenerate", "长沙"))
        self.start_add.setItemText(5, _translate("TableGenerate", "厦门"))
        self.start_add.setItemText(6, _translate("TableGenerate", "成都"))
        self.start_add.setItemText(7, _translate("TableGenerate", "青岛"))
        self.start_add.setItemText(8, _translate("TableGenerate", "沈阳"))
        self.start_add.setItemText(9, _translate("TableGenerate", "上海"))
        self.start_add.setItemText(10, _translate("TableGenerate", "河南"))
        self.start_add.setItemText(11, _translate("TableGenerate", "海宁"))
        self.start_add.setItemText(12, _translate("TableGenerate", "其他..."))
        self.label_18.setText(_translate("TableGenerate", "件"))
        self.package_label.setText(_translate("TableGenerate", "包装"))
        self.label_7.setText(_translate("TableGenerate", "地址"))
        self.label_6.setText(_translate("TableGenerate", "收货人"))
        self.label_3.setText(_translate("TableGenerate", "网络单位"))
        self.network_department.setCurrentText(_translate("TableGenerate", "中达"))
        self.network_department.setItemText(0, _translate("TableGenerate", "中达"))
        self.network_department.setItemText(1, _translate("TableGenerate", "龙航"))
        self.network_department.setItemText(2, _translate("TableGenerate", "星云"))
        self.network_department.setItemText(3, _translate("TableGenerate", "泰保"))
        self.network_department.setItemText(4, _translate("TableGenerate", "荟运"))
        self.network_department.setItemText(5, _translate("TableGenerate", "邓星宇"))
        self.network_department.setItemText(6, _translate("TableGenerate", "林翔"))
        self.network_department.setItemText(7, _translate("TableGenerate", "北涛"))
        self.network_department.setItemText(8, _translate("TableGenerate", "邦德"))
        self.network_department.setItemText(9, _translate("TableGenerate", "金京信"))
        self.network_department.setItemText(10, _translate("TableGenerate", "迪瑞宝"))
        self.network_department.setItemText(11, _translate("TableGenerate", "天翔"))
        self.network_department.setItemText(12, _translate("TableGenerate", "商舟"))
        self.network_department.setItemText(13, _translate("TableGenerate", "顺捷"))
        self.network_department.setItemText(14, _translate("TableGenerate", "诚誉"))
        self.network_department.setItemText(15, _translate("TableGenerate", "浩通"))
        self.network_department.setItemText(16, _translate("TableGenerate", "弘运"))
        self.network_department.setItemText(17, _translate("TableGenerate", "其他..."))
        self.label_17.setText(_translate("TableGenerate", "电话"))
        self.label_8.setText(_translate("TableGenerate", "品名"))
        self.transfer_fee_label.setText(_translate("TableGenerate", "中转费"))
        self.total_money_label.setText(_translate("TableGenerate", "合计金额"))
        self.label.setText(_translate("TableGenerate", "表单日期"))
        self.self_fee_label.setText(_translate("TableGenerate", "自提费"))
        self.label_4.setText(_translate("TableGenerate", "始发地"))
        self.delivery_cost_label.setText(_translate("TableGenerate", "配送费"))
        self.label_9.setText(_translate("TableGenerate", "数量与重量"))
        self.label_5.setText(_translate("TableGenerate", "单号"))
        self.payment_method_label.setText(_translate("TableGenerate", "付款方式"))
        self.label_2.setText(_translate("TableGenerate", "No."))
        self.calcButton.setText(_translate("TableGenerate", "自动计算"))
        self.OK_Button.setText(_translate("TableGenerate", "生成"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.input_tab), _translate("TableGenerate", "表单生成"))
        self.pushButton_ocr.setText(_translate("TableGenerate", "选择图片"))
        self.ocr_network.setItemText(1, _translate("TableGenerate", "龙航"))
        self.ocr_network.setItemText(2, _translate("TableGenerate", "顺捷"))
        self.ocr_network.setItemText(3, _translate("TableGenerate", "林翔"))
        self.orc_network_label.setText(_translate("TableGenerate", "网络单位"))
        self.ocr_label.setText(_translate("TableGenerate", "图片识别信息"))
        self.ocr_button.setText(_translate("TableGenerate", "生成"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.ocr_tab), _translate("TableGenerate", "图像识别"))
        self.label_merge.setText(_translate("TableGenerate", "待合并文件"))
        self.pushButton_addmerge.setText(_translate("TableGenerate", "添加"))
        self.pushButton_merge.setText(_translate("TableGenerate", "合并"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.merge_tab), _translate("TableGenerate", "表单合并"))
