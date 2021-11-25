# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\tablegenerate.ui'
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
        self.No = QtWidgets.QTextEdit(TableGenerate)
        self.No.setGeometry(QtCore.QRect(110, 120, 231, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.No.setFont(font)
        self.No.setObjectName("No")
        self.network_department_other = QtWidgets.QTextEdit(TableGenerate)
        self.network_department_other.setGeometry(QtCore.QRect(250, 180, 91, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.network_department_other.setFont(font)
        self.network_department_other.setObjectName("network_department_other")
        self.start_add_other = QtWidgets.QTextEdit(TableGenerate)
        self.start_add_other.setGeometry(QtCore.QRect(250, 240, 91, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.start_add_other.setFont(font)
        self.start_add_other.setObjectName("start_add_other")
        self.code = QtWidgets.QTextEdit(TableGenerate)
        self.code.setGeometry(QtCore.QRect(110, 300, 231, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.code.setFont(font)
        self.code.setObjectName("code")
        self.people_name = QtWidgets.QTextEdit(TableGenerate)
        self.people_name.setGeometry(QtCore.QRect(110, 360, 231, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.people_name.setFont(font)
        self.people_name.setObjectName("people_name")
        self.add = QtWidgets.QTextEdit(TableGenerate)
        self.add.setGeometry(QtCore.QRect(110, 420, 231, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.add.setFont(font)
        self.add.setObjectName("add")
        self.dateEdit = QtWidgets.QDateEdit(TableGenerate)
        self.dateEdit.setGeometry(QtCore.QRect(110, 60, 231, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.dateEdit.setFont(font)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setObjectName("dateEdit")
        self.count = QtWidgets.QDoubleSpinBox(TableGenerate)
        self.count.setGeometry(QtCore.QRect(460, 120, 91, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.count.setFont(font)
        self.count.setObjectName("count")
        self.weight = QtWidgets.QDoubleSpinBox(TableGenerate)
        self.weight.setGeometry(QtCore.QRect(590, 120, 101, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.weight.setFont(font)
        self.weight.setObjectName("weight")
        self.package = QtWidgets.QDoubleSpinBox(TableGenerate)
        self.package.setGeometry(QtCore.QRect(460, 220, 91, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.package.setFont(font)
        self.package.setMaximum(999999.99)
        self.package.setObjectName("package")
        self.agency_fund = QtWidgets.QDoubleSpinBox(TableGenerate)
        self.agency_fund.setGeometry(QtCore.QRect(460, 260, 91, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.agency_fund.setFont(font)
        self.agency_fund.setMaximum(999999.99)
        self.agency_fund.setObjectName("agency_fund")
        self.delivery_cost = QtWidgets.QDoubleSpinBox(TableGenerate)
        self.delivery_cost.setGeometry(QtCore.QRect(460, 300, 91, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.delivery_cost.setFont(font)
        self.delivery_cost.setMaximum(999999.99)
        self.delivery_cost.setObjectName("delivery_cost")
        self.self_fee = QtWidgets.QDoubleSpinBox(TableGenerate)
        self.self_fee.setGeometry(QtCore.QRect(460, 340, 91, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.self_fee.setFont(font)
        self.self_fee.setMaximum(999999.99)
        self.self_fee.setObjectName("self_fee")
        self.transfer_fee = QtWidgets.QDoubleSpinBox(TableGenerate)
        self.transfer_fee.setGeometry(QtCore.QRect(460, 380, 91, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.transfer_fee.setFont(font)
        self.transfer_fee.setMaximum(999999.99)
        self.transfer_fee.setObjectName("transfer_fee")
        self.payment_method = QtWidgets.QTextEdit(TableGenerate)
        self.payment_method.setGeometry(QtCore.QRect(460, 430, 231, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.payment_method.setFont(font)
        self.payment_method.setObjectName("payment_method")
        self.money = QtWidgets.QDoubleSpinBox(TableGenerate)
        self.money.setGeometry(QtCore.QRect(460, 490, 111, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.money.setFont(font)
        self.money.setMaximum(999999.99)
        self.money.setObjectName("money")
        self.label = QtWidgets.QLabel(TableGenerate)
        self.label.setGeometry(QtCore.QRect(20, 60, 80, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(TableGenerate)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 54, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(TableGenerate)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 80, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(TableGenerate)
        self.label_4.setGeometry(QtCore.QRect(20, 240, 80, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(TableGenerate)
        self.label_5.setGeometry(QtCore.QRect(20, 300, 54, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(TableGenerate)
        self.label_6.setGeometry(QtCore.QRect(20, 360, 80, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(TableGenerate)
        self.label_7.setGeometry(QtCore.QRect(20, 420, 54, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(TableGenerate)
        self.label_8.setGeometry(QtCore.QRect(370, 60, 95, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(TableGenerate)
        self.label_9.setGeometry(QtCore.QRect(355, 120, 100, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(TableGenerate)
        self.label_10.setGeometry(QtCore.QRect(370, 220, 95, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(TableGenerate)
        self.label_11.setGeometry(QtCore.QRect(370, 260, 95, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(TableGenerate)
        self.label_12.setGeometry(QtCore.QRect(370, 300, 95, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(TableGenerate)
        self.label_13.setGeometry(QtCore.QRect(370, 340, 95, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(TableGenerate)
        self.label_14.setGeometry(QtCore.QRect(370, 380, 95, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(TableGenerate)
        self.label_15.setGeometry(QtCore.QRect(370, 430, 95, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(TableGenerate)
        self.label_16.setGeometry(QtCore.QRect(370, 490, 95, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.phone_number = QtWidgets.QTextEdit(TableGenerate)
        self.phone_number.setGeometry(QtCore.QRect(110, 480, 231, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.phone_number.setFont(font)
        self.phone_number.setObjectName("phone_number")
        self.label_17 = QtWidgets.QLabel(TableGenerate)
        self.label_17.setGeometry(QtCore.QRect(20, 480, 54, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.goods_name = QtWidgets.QTextEdit(TableGenerate)
        self.goods_name.setGeometry(QtCore.QRect(460, 60, 231, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.goods_name.setFont(font)
        self.goods_name.setObjectName("goods_name")
        self.label_18 = QtWidgets.QLabel(TableGenerate)
        self.label_18.setGeometry(QtCore.QRect(560, 120, 54, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(TableGenerate)
        self.label_19.setGeometry(QtCore.QRect(700, 120, 54, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.start_add = QtWidgets.QComboBox(TableGenerate)
        self.start_add.setGeometry(QtCore.QRect(110, 240, 121, 31))
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
        self.network_department = QtWidgets.QComboBox(TableGenerate)
        self.network_department.setGeometry(QtCore.QRect(110, 180, 121, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.network_department.setFont(font)
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
        self.OK_Button = QtWidgets.QPushButton(TableGenerate)
        self.OK_Button.setGeometry(QtCore.QRect(550, 570, 75, 32))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.OK_Button.setFont(font)
        self.OK_Button.setObjectName("OK_Button")
        self.cancel_Button = QtWidgets.QPushButton(TableGenerate)
        self.cancel_Button.setGeometry(QtCore.QRect(630, 570, 75, 32))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.cancel_Button.setFont(font)
        self.cancel_Button.setObjectName("cancel_Button")
        self.toolButton = QtWidgets.QToolButton(TableGenerate)
        self.toolButton.setGeometry(QtCore.QRect(466, 570, 41, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.toolButton.setFont(font)
        self.toolButton.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        self.toolButton.setObjectName("toolButton")
        self.label_20 = QtWidgets.QLabel(TableGenerate)
        self.label_20.setGeometry(QtCore.QRect(10, 570, 101, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(12)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.dir_path = QtWidgets.QLineEdit(TableGenerate)
        self.dir_path.setGeometry(QtCore.QRect(120, 570, 331, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(13)
        self.dir_path.setFont(font)
        self.dir_path.setObjectName("dir_path")
        self.calcButton = QtWidgets.QPushButton(TableGenerate)
        self.calcButton.setGeometry(QtCore.QRect(600, 490, 91, 31))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(13)
        self.calcButton.setFont(font)
        self.calcButton.setObjectName("calcButton")

        self.retranslateUi(TableGenerate)
        self.network_department.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TableGenerate)
        TableGenerate.setTabOrder(self.dateEdit, self.No)
        TableGenerate.setTabOrder(self.No, self.network_department)
        TableGenerate.setTabOrder(self.network_department, self.network_department_other)
        TableGenerate.setTabOrder(self.network_department_other, self.start_add)
        TableGenerate.setTabOrder(self.start_add, self.start_add_other)
        TableGenerate.setTabOrder(self.start_add_other, self.code)
        TableGenerate.setTabOrder(self.code, self.people_name)
        TableGenerate.setTabOrder(self.people_name, self.add)
        TableGenerate.setTabOrder(self.add, self.phone_number)
        TableGenerate.setTabOrder(self.phone_number, self.goods_name)
        TableGenerate.setTabOrder(self.goods_name, self.count)
        TableGenerate.setTabOrder(self.count, self.weight)
        TableGenerate.setTabOrder(self.weight, self.package)
        TableGenerate.setTabOrder(self.package, self.agency_fund)
        TableGenerate.setTabOrder(self.agency_fund, self.delivery_cost)
        TableGenerate.setTabOrder(self.delivery_cost, self.self_fee)
        TableGenerate.setTabOrder(self.self_fee, self.transfer_fee)
        TableGenerate.setTabOrder(self.transfer_fee, self.payment_method)
        TableGenerate.setTabOrder(self.payment_method, self.money)
        TableGenerate.setTabOrder(self.money, self.toolButton)
        TableGenerate.setTabOrder(self.toolButton, self.OK_Button)
        TableGenerate.setTabOrder(self.OK_Button, self.cancel_Button)

    def retranslateUi(self, TableGenerate):
        _translate = QtCore.QCoreApplication.translate
        TableGenerate.setWindowTitle(_translate("TableGenerate", "Table Generator v1.0    -by Y.H."))
        self.dateEdit.setDisplayFormat(_translate("TableGenerate", "yyyy-MM-dd"))
        self.label.setText(_translate("TableGenerate", "表单日期"))
        self.label_2.setText(_translate("TableGenerate", "No."))
        self.label_3.setText(_translate("TableGenerate", "网络单位"))
        self.label_4.setText(_translate("TableGenerate", "始发地"))
        self.label_5.setText(_translate("TableGenerate", "单号"))
        self.label_6.setText(_translate("TableGenerate", "收货人"))
        self.label_7.setText(_translate("TableGenerate", "地址"))
        self.label_8.setText(_translate("TableGenerate", "品名"))
        self.label_9.setText(_translate("TableGenerate", "数量与重量"))
        self.label_10.setText(_translate("TableGenerate", "包装"))
        self.label_11.setText(_translate("TableGenerate", "代收款"))
        self.label_12.setText(_translate("TableGenerate", "配送费"))
        self.label_13.setText(_translate("TableGenerate", "自提费"))
        self.label_14.setText(_translate("TableGenerate", "中转费"))
        self.label_15.setText(_translate("TableGenerate", "付款方式"))
        self.label_16.setText(_translate("TableGenerate", "合计金额"))
        self.label_17.setText(_translate("TableGenerate", "电话"))
        self.label_18.setText(_translate("TableGenerate", "件"))
        self.label_19.setText(_translate("TableGenerate", "KG"))
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
        self.network_department.setCurrentText(_translate("TableGenerate", "中达"))
        self.network_department.setItemText(0, _translate("TableGenerate", "中达"))
        self.network_department.setItemText(1, _translate("TableGenerate", "龙杭"))
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
        self.network_department.setItemText(12, _translate("TableGenerate", "商周"))
        self.network_department.setItemText(13, _translate("TableGenerate", "顺捷"))
        self.network_department.setItemText(14, _translate("TableGenerate", "诚誉"))
        self.network_department.setItemText(15, _translate("TableGenerate", "浩通"))
        self.network_department.setItemText(16, _translate("TableGenerate", "弘运"))
        self.network_department.setItemText(17, _translate("TableGenerate", "其他..."))
        self.OK_Button.setText(_translate("TableGenerate", "生成"))
        self.cancel_Button.setText(_translate("TableGenerate", "退出"))
        self.toolButton.setText(_translate("TableGenerate", "..."))
        self.label_20.setText(_translate("TableGenerate", "文件保存位置"))
        self.calcButton.setText(_translate("TableGenerate", "自动计算"))
