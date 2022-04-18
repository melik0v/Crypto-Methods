# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'atbash.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

# ALPHABETS:
# Digital
digit_alph = [str(_) for _ in range(0, 10)]

# English lowercase
en_alph_lower = list(map(chr, range(ord('a'), ord('z') + 1)))

# English uppercase
en_alph_upper = list(map(chr, range(ord('A'), ord('Z') + 1)))

# Russian lowercase
ru_alph_lower = list(map(chr, range(ord('а'), ord('я') + 1)))
ru_alph_lower.insert(6, 'ё')

# Russian uppercase
ru_alph_upper = list(map(chr, range(ord('А'), ord('Я') + 1)))
ru_alph_upper.insert(6, 'Ё')


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(685, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(685, 540))
        MainWindow.setMaximumSize(QtCore.QSize(685, 540))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0,0);")
        self.centralwidget.setObjectName("centralwidget")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(490, 310, 61, 30))
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
        self.decrypt_btn.setGeometry(QtCore.QRect(280, 480, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.decrypt_btn.setFont(font)
        self.decrypt_btn.setStyleSheet("QPushButton {\n"
                                       "    color: black;\n"
                                       "    background-color: grey;\n"
                                       "    border-radius: 7px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(102, 102, 102);\n"
                                       "}")
        self.decrypt_btn.setObjectName("decrypt_btn")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(460, 50, 151, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(87)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color: white;\n"
                                   "font: 14pt \"Century Gothic\";\n"
                                   "font-weight: 700;")
        self.label_9.setObjectName("label_9")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 269, 701, 41))
        self.frame_2.setAutoFillBackground(False)
        self.frame_2.setStyleSheet("background-color: rgb(49, 80, 78)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(220, 0, 271, 41))
        self.label_7.setStyleSheet("color: white;\n"
                                   "font: 18pt \"Century Gothic\";\n"
                                   "font-weight: 700;")
        self.label_7.setObjectName("label_7")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 701, 41))
        self.frame.setStyleSheet("background-color: rgb(49, 80, 78)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(240, 0, 211, 41))
        self.label_4.setStyleSheet("color: white;\n"
                                   "font: 18pt \"Century Gothic\";\n"
                                   "font-weight: 700;")
        self.label_4.setObjectName("label_4")
        self.encrypt_btn = QtWidgets.QPushButton(self.centralwidget)
        self.encrypt_btn.setGeometry(QtCore.QRect(280, 220, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.encrypt_btn.setFont(font)
        self.encrypt_btn.setStyleSheet("QPushButton {\n"
                                       "    color: black;\n"
                                       "    background-color: grey;\n"
                                       "    border-radius: 7px;\n"
                                       "}\n"
                                       "\n"
                                       "QPushButton:pressed {\n"
                                       "    background-color: rgb(102, 102, 102);\n"
                                       "}")
        self.encrypt_btn.setObjectName("encrypt_btn")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(120, 50, 61, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: white;\n"
                                   "")
        self.label_8.setObjectName("label_8")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(90, 310, 151, 30))
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
        self.text_edit_encrypted = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_edit_encrypted.setGeometry(QtCore.QRect(20, 340, 290, 120))
        self.text_edit_encrypted.setStyleSheet("background-color: rgb(42, 42, 42);\n"
                                               "border: 1px solid gray;\n"
                                               "border-radius: 10px;\n"
                                               "color: white;\n"
                                               "")
        self.text_edit_encrypted.setObjectName("text_edit_encrypted")
        self.textBrowser_encrypted = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_encrypted.setGeometry(QtCore.QRect(380, 80, 290, 120))
        self.textBrowser_encrypted.setStyleSheet("background-color: rgb(42, 42, 42);\n"
                                                 "border: 1px solid gray;\n"
                                                 "border-radius: 10px;\n"
                                                 "color: white;\n"
                                                 "")
        self.textBrowser_encrypted.setObjectName("textBrowser_encrypted")
        self.textBrowser_decrypted = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_decrypted.setGeometry(QtCore.QRect(380, 340, 290, 120))
        self.textBrowser_decrypted.setStyleSheet("background-color: rgb(42, 42, 42);\n"
                                                 "border: 1px solid gray;\n"
                                                 "border-radius: 10px;\n"
                                                 "color: white;\n"
                                                 "")
        self.textBrowser_decrypted.setObjectName("textBrowser_decrypted")
        self.text_edit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.text_edit.setGeometry(QtCore.QRect(20, 80, 290, 120))
        self.text_edit.setStyleSheet("background-color: rgb(42, 42, 42);\n"
                                     "border: 1px solid gray;\n"
                                     "border-radius: 10px;\n"
                                     "color: white;\n"
                                     "")
        self.text_edit.setObjectName("text_edit")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Activating buttons
        self.activate_btns()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Атбаш"))
        self.label_10.setText(_translate("MainWindow", "Текст"))
        self.decrypt_btn.setText(_translate("MainWindow", "Расшифровать"))
        self.label_9.setText(_translate("MainWindow", "ШИФРОТЕКСТ"))
        self.label_7.setText(_translate("MainWindow", "РАСШИФРОВАНИЕ"))
        self.label_4.setText(_translate("MainWindow", "ШИФРОВАНИЕ"))
        self.encrypt_btn.setText(_translate("MainWindow", "Зашифровать"))
        self.label_8.setText(_translate("MainWindow", "ТЕКСТ"))
        self.label_11.setText(_translate("MainWindow", "Шифротекст"))

    def activate_btns(self):
        self.encrypt_btn.clicked.connect(lambda: self.encrypt(self.text_edit.toPlainText()))
        self.decrypt_btn.clicked.connect(lambda: self.decrypt(self.text_edit_encrypted.toPlainText()))

    def encrypt(self, text):
        encrypted_text = ""
        for i in text:
            for ch in digit_alph:
                if i == ch:
                    pos = digit_alph.index(ch)
                    encrypted_text += digit_alph[len(digit_alph) - pos - 1]

            for ch in en_alph_lower:
                if i == ch:
                    pos = en_alph_lower.index(ch)
                    encrypted_text += en_alph_lower[len(en_alph_lower) - pos - 1]

            for ch in en_alph_upper:
                if i == ch:
                    pos = en_alph_upper.index(ch)
                    encrypted_text += en_alph_upper[len(en_alph_upper) - pos - 1]

            for ch in ru_alph_lower:
                if i == ch:
                    pos = ru_alph_lower.index(ch)
                    encrypted_text += ru_alph_lower[len(ru_alph_lower) - pos - 1]

            for ch in ru_alph_upper:
                if i == ch:
                    pos = ru_alph_upper.index(ch)
                    encrypted_text += ru_alph_upper[len(ru_alph_upper) - pos - 1]

            if i not in digit_alph and i not in ru_alph_lower and i not in ru_alph_upper and i not in en_alph_lower \
                    and i not in en_alph_upper:
                encrypted_text += i

        self.textBrowser_encrypted.setPlainText(encrypted_text)

    def decrypt(self, text):
        decrypted_text = ""

        for i in text:
            for ch in digit_alph:
                if i == ch:
                    pos = digit_alph.index(ch)
                    decrypted_text += digit_alph[len(digit_alph) - pos - 1]

            for ch in en_alph_lower:
                if i == ch:
                    pos = en_alph_lower.index(ch)
                    decrypted_text += en_alph_lower[len(en_alph_lower) - pos - 1]

            for ch in en_alph_upper:
                if i == ch:
                    pos = en_alph_upper.index(ch)
                    decrypted_text += en_alph_upper[len(en_alph_upper) - pos - 1]

            for ch in ru_alph_lower:
                if i == ch:
                    pos = ru_alph_lower.index(ch)
                    decrypted_text += ru_alph_lower[len(ru_alph_lower) - pos - 1]

            for ch in ru_alph_upper:
                if i == ch:
                    pos = ru_alph_upper.index(ch)
                    decrypted_text += ru_alph_upper[len(ru_alph_upper) - pos - 1]

            if i not in digit_alph and i not in ru_alph_lower and i not in ru_alph_upper and i not in en_alph_lower \
                    and i not in en_alph_upper:
                decrypted_text += i

        self.textBrowser_decrypted.setPlainText(decrypted_text)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
