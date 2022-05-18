# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '13.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
from lab_13 import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1110, 855)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(685, 540))
        MainWindow.setMaximumSize(QtCore.QSize(1110, 855))
        MainWindow.setStyleSheet("background-color: rgb(170, 170, 170);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: #2B2B2B;")
        self.centralwidget.setObjectName("centralwidget")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(740, 200, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: white;\n"
"font: 14pt \"Century Gothic\";\n"
"font-weight: 700;\n"
"text-transform: uppercase;\n"
"")
        self.label_10.setObjectName("label_10")
        self.decrypt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.decrypt_btn.setGeometry(QtCore.QRect(390, 311, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.decrypt_btn.setFont(font)
        self.decrypt_btn.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: grey;\n"
"    border-radius: 7px;\n"
"    border-color: black;\n"
"    border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(102, 102, 102);\n"
"}")
        self.decrypt_btn.setObjectName("decrypt_btn")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1121, 41))
        self.frame.setStyleSheet("background-color: rgb(49, 80, 78)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(345, 0, 411, 41))
        self.label_4.setStyleSheet("color: white;\n"
"font: 18pt \"Century Gothic\";\n"
"font-weight: 700;")
        self.label_4.setObjectName("label_4")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(130, 201, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: white;\n"
"font: 14pt \"Century Gothic\";\n"
"font-weight: 700;\n"
"text-transform: uppercase;\n"
"")
        self.label_11.setObjectName("label_11")
        self.InputFile_btn = QtWidgets.QPushButton(self.centralwidget)
        self.InputFile_btn.setGeometry(QtCore.QRect(30, 231, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.InputFile_btn.setFont(font)
        self.InputFile_btn.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: grey;\n"
"    border-radius: 7px;\n"
"    border-color: black;\n"
"    border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(102, 102, 102);\n"
"}")
        self.InputFile_btn.setObjectName("InputFile_btn")
        self.input_path = QtWidgets.QLabel(self.centralwidget)
        self.input_path.setGeometry(QtCore.QRect(160, 231, 311, 30))
        self.input_path.setStyleSheet("color: white;\n"
"background-color: black;\n"
"font: 14pt \"Century Gothic\";\n"
"font-weight: 700;\n"
"text-transform: uppercase;\n"
"")
        self.input_path.setObjectName("input_path")
        self.Open_InputFile_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Open_InputFile_btn.setGeometry(QtCore.QRect(30, 271, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.Open_InputFile_btn.setFont(font)
        self.Open_InputFile_btn.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: grey;\n"
"    border-radius: 7px;\n"
"    border-color: black;\n"
"    border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(102, 102, 102);\n"
"}")
        self.Open_InputFile_btn.setObjectName("Open_InputFile_btn")
        self.Open_OutputFile_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Open_OutputFile_btn.setGeometry(QtCore.QRect(550, 271, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.Open_OutputFile_btn.setFont(font)
        self.Open_OutputFile_btn.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: grey;\n"
"    border-radius: 7px;\n"
"    border-color: black;\n"
"    border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(102, 102, 102);\n"
"}")
        self.Open_OutputFile_btn.setObjectName("Open_OutputFile_btn")
        self.OutputFile_btn = QtWidgets.QPushButton(self.centralwidget)
        self.OutputFile_btn.setGeometry(QtCore.QRect(550, 231, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.OutputFile_btn.setFont(font)
        self.OutputFile_btn.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: grey;\n"
"    border-radius: 7px;\n"
"    border-color: black;\n"
"    border: 1px solid;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(102, 102, 102);\n"
"}")
        self.OutputFile_btn.setObjectName("OutputFile_btn")
        self.output_path = QtWidgets.QLabel(self.centralwidget)
        self.output_path.setGeometry(QtCore.QRect(680, 231, 301, 30))
        self.output_path.setStyleSheet("color: white;\n"
"background-color: black;\n"
"font: 14pt \"Century Gothic\";\n"
"font-weight: 700;\n"
"text-transform: uppercase;\n"
"")
        self.output_path.setObjectName("output_path")
        self.widget = PlotWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(4, 41, 1101, 150))
        self.widget.setStyleSheet("background-color: black;")
        self.widget.setObjectName("widget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(986, 191, 122, 661))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("alternate-background-color: rgb(0, 0, 0);\n"
"color: white;\n"
"background-color: black;\n"
"gridline-color: grey;\n"
"text-align: center;")
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(26)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(50)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(33)
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 361, 961, 491))
        self.textBrowser.setStyleSheet("border: 1px solid;\n"
"border-color: grey;\n"
"background-color: black;\n"
"color: white;")
        self.textBrowser.setObjectName("textBrowser")
        self.lang_name = QtWidgets.QLabel(self.centralwidget)
        self.lang_name.setGeometry(QtCore.QRect(30, 310, 61, 31))
        self.lang_name.setStyleSheet("color: white;\n"
"background-color: black;\n"
"font: 14pt \"Century Gothic\";\n"
"font-weight: 700;\n"
"text-transform: uppercase;\n"
"")
        self.lang_name.setObjectName("lang_name")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.addItem('RUS')
        self.comboBox.addItem('ENG')
        self.comboBox.setGeometry(QtCore.QRect(100, 310, 70, 31))
        self.comboBox.setStyleSheet("background-color: black;\n"
"color: white;\n"
"font-family: Century Gothic;\n"
"font-size: 14px;")
        self.comboBox.setObjectName("comboBox")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_10.setText(_translate("MainWindow", "Текст"))
        self.decrypt_btn.setText(_translate("MainWindow", "Дешифровать"))
        self.label_4.setText(_translate("MainWindow", "ЧАСТОТНЫЙ КРИПТОАНАЛИЗ"))
        self.label_11.setText(_translate("MainWindow", "Шифротекст"))
        self.InputFile_btn.setText(_translate("MainWindow", "Входной файл"))
        self.input_path.setText(_translate("MainWindow", "NO INPUT FILE"))
        self.Open_InputFile_btn.setText(_translate("MainWindow", "Открыть"))
        self.Open_OutputFile_btn.setText(_translate("MainWindow", "Открыть"))
        self.OutputFile_btn.setText(_translate("MainWindow", "Выходной файл"))
        self.output_path.setText(_translate("MainWindow", "NO OUTPUT FILE"))
        self.lang_name.setText(_translate("MainWindow", "ЯЗЫК"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = FreqAnalisys()
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
