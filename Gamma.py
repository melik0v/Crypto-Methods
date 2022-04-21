from random import randint
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from os import path
from typing import Generator


class GammaError(Exception):
    pass


def generate_key(length: int) -> str:
    key = []
    j = 0
    seed = randint(0, 10 ** 10)
    for i in lcg(256, 1103515245, 12345, seed):
        key.append(chr(i))
        j += 1
        if j == length - 1:
            break
    return ''.join(key)


def lcg(modulus: int, a: int, c: int, seed: int) -> Generator[int, None, None]:
    """Linear congruential generator."""
    while True:
        seed = (a * seed + c) % modulus
        yield seed


def gamma(text, key):
    """
    Gamma cipher (charset: KOI8-r)

    :param text: Text to be encrypted/decrypted
    :param key: Key of encryption
    :return:
    """
    if not text:
        return "Input text is empty!"

    if not key:
        return "The key is missing!"

        # attempt to change the encoding of the input text
    try:
        text_bytes = bytearray(text, encoding="KOI8-r")

    except UnicodeEncodeError:
        return "Invalid character in input text! (KOI8-r)"

        # attempt to change key encoding
    try:
        key_bytes = bytearray(key, encoding="KOI8-r", errors='replace')

    except UnicodeEncodeError:
        return "Invalid character in key! (KOI8-r)"

    for i in range(len(text_bytes)):
        text_bytes[i] ^= key_bytes[i % len(key_bytes)]

    try:
        modified_text = text_bytes.decode("KOI8-r")

    except UnicodeDecodeError:
        return "Decoding error! (from 'KOI8-r')"

    return modified_text


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(685, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(685, 650))
        MainWindow.setMaximumSize(QtCore.QSize(685, 650))
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0,0);")
        self.centralwidget.setObjectName("centralwidget")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(490, 400, 61, 30))
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
        self.decrypt_btn.setGeometry(QtCore.QRect(520, 570, 130, 30))
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
        self.frame_2.setGeometry(QtCore.QRect(0, 359, 701, 41))
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
        self.encrypt_btn.setGeometry(QtCore.QRect(520, 220, 130, 30))
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
        self.label_11.setGeometry(QtCore.QRect(90, 400, 151, 30))
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
        self.text_edit_encrypted.setGeometry(QtCore.QRect(20, 430, 290, 120))
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
        self.textBrowser_decrypted.setGeometry(QtCore.QRect(380, 430, 290, 120))
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 230, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: white;")
        self.label.setObjectName("label")
        self.InputFile_btn = QtWidgets.QPushButton(self.centralwidget)
        self.InputFile_btn.setGeometry(QtCore.QRect(20, 570, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.InputFile_btn.setFont(font)
        self.InputFile_btn.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: grey;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(102, 102, 102);\n"
"}")
        self.InputFile_btn.setObjectName("InputFile_btn")
        self.OutputFile_btn = QtWidgets.QPushButton(self.centralwidget)
        self.OutputFile_btn.setGeometry(QtCore.QRect(20, 610, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.OutputFile_btn.setFont(font)
        self.OutputFile_btn.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: grey;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(102, 102, 102);\n"
"}")
        self.OutputFile_btn.setObjectName("OutputFile_btn")
        self.input_path = QtWidgets.QLabel(self.centralwidget)
        self.input_path.setGeometry(QtCore.QRect(160, 570, 311, 30))
        self.input_path.setStyleSheet("color: white;\n"
"font: 14pt \"Century Gothic\";\n"
"font-weight: 700;\n"
"text-transform: uppercase;\n"
"")
        self.input_path.setObjectName("input_path")
        self.output_path = QtWidgets.QLabel(self.centralwidget)
        self.output_path.setGeometry(QtCore.QRect(160, 610, 311, 30))
        self.output_path.setStyleSheet("color: white;\n"
"font: 14pt \"Century Gothic\";\n"
"font-weight: 700;\n"
"text-transform: uppercase;\n"
"")
        self.output_path.setObjectName("output_path")
        self.OutputFile_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.OutputFile_btn_2.setGeometry(QtCore.QRect(20, 310, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.OutputFile_btn_2.setFont(font)
        self.OutputFile_btn_2.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: grey;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(102, 102, 102);\n"
"}")
        self.OutputFile_btn_2.setObjectName("OutputFile_btn_2")
        self.input_path_2 = QtWidgets.QLabel(self.centralwidget)
        self.input_path_2.setGeometry(QtCore.QRect(160, 270, 311, 30))
        self.input_path_2.setStyleSheet("color: white;\n"
"font: 14pt \"Century Gothic\";\n"
"font-weight: 700;\n"
"text-transform: uppercase;\n"
"")
        self.input_path_2.setObjectName("input_path_2")
        self.output_path_2 = QtWidgets.QLabel(self.centralwidget)
        self.output_path_2.setGeometry(QtCore.QRect(160, 310, 311, 30))
        self.output_path_2.setStyleSheet("color: white;\n"
"font: 14pt \"Century Gothic\";\n"
"font-weight: 700;\n"
"text-transform: uppercase;\n"
"")
        self.output_path_2.setObjectName("output_path_2")
        self.InputFile_btn_2 = QtWidgets.QPushButton(self.centralwidget)
        self.InputFile_btn_2.setGeometry(QtCore.QRect(20, 270, 120, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        self.InputFile_btn_2.setFont(font)
        self.InputFile_btn_2.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: grey;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(102, 102, 102);\n"
"}")
        self.InputFile_btn_2.setObjectName("InputFile_btn_2")
#         self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
#         self.checkBox.setGeometry(QtCore.QRect(435, 225, 80, 20))
#         self.checkBox.setStyleSheet("color: white;\n"
# "font: 14pt \"Century Gothic\";\n"
# "font-weight: 700;\n"
# "text-transform: uppercase;\n"
# "")
#         self.checkBox.setObjectName("checkBox")
        self.key_btn = QtWidgets.QPushButton(self.centralwidget)
        self.key_btn.setGeometry(QtCore.QRect(100, 224, 31, 30))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.key_btn.setFont(font)
        self.key_btn.setStyleSheet("QPushButton {\n"
"    color: black;\n"
"    background-color: grey;\n"
"    border-radius: 7px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(102, 102, 102);\n"
"}")
        self.key_btn.setObjectName("key_btn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 230, 250, 16))
        self.label_2.setStyleSheet("color: white;\n"
"font: 14pt \"Century Gothic\";\n"
"font-weight: 700;\n"
"text-transform: uppercase;\n"
"")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gamma"))
        self.label_10.setText(_translate("MainWindow", "Текст"))
        self.decrypt_btn.setText(_translate("MainWindow", "Расшифровать"))
        self.label_9.setText(_translate("MainWindow", "ШИФРОТЕКСТ"))
        self.label_7.setText(_translate("MainWindow", "РАСШИФРОВАНИЕ"))
        self.label_4.setText(_translate("MainWindow", "ШИФРОВАНИЕ"))
        self.encrypt_btn.setText(_translate("MainWindow", "Зашифровать"))
        self.label_8.setText(_translate("MainWindow", "ТЕКСТ"))
        self.label_11.setText(_translate("MainWindow", "Шифротекст"))
        self.label.setText(_translate("MainWindow", "КЛЮЧ"))
        self.InputFile_btn.setText(_translate("MainWindow", "Входной файл"))
        self.OutputFile_btn.setText(_translate("MainWindow", "Выходной файл"))
        self.input_path.setText(_translate("MainWindow", "NO INPUT FILE"))
        self.output_path.setText(_translate("MainWindow", "NO OUTPUT FILE"))
        self.OutputFile_btn_2.setText(_translate("MainWindow", "Выходной файл"))
        self.input_path_2.setText(_translate("MainWindow", "NO INPUT FILE"))
        self.output_path_2.setText(_translate("MainWindow", "NO OUTPUT FILE"))
        self.InputFile_btn_2.setText(_translate("MainWindow", "Входной файл"))
        # self.checkBox.setText(_translate("MainWindow", "AUTO"))
        self.key_btn.setText(_translate("MainWindow", "..."))
        self.label_2.setText(_translate("MainWindow", "NO KEY"))


class Gamma(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Gamma, self).__init__()
        self.setupUi(self)
        self.functions()

    def open_file_dialog_box(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Open File', './txt', "Text file (*.txt)")
        return path.basename(file)

    def change_input_files_labels(self, function: str):
        filename = self.open_file_dialog_box()
        if function == 'encrypt':
            if filename == '':
                self.input_path_2.setText('NO INPUT FILE')
            else:
                self.input_path_2.setText(filename)
        elif function == 'decrypt':
            if filename == '':
                self.input_path.setText('NO INPUT FILE')
            else:
                self.input_path.setText(filename)

    def change_output_files_labels(self, function: str):
        filename = self.open_file_dialog_box()
        if function == 'encrypt':
            if filename == '':
                self.output_path_2.setText('NO OUTPUT FILE')
            else:
                self.output_path_2.setText(filename)
                self.input_path.setText(filename)
        elif function == 'decrypt':
            if filename == '':
                self.output_path.setText('NO OUTPUT FILE')
            else:
                self.output_path.setText(filename)

    def open_key_file(self):
        filename = self.open_file_dialog_box()
        if filename == '':
            self.label_2.setText("NO KEY")
        else:
            self.label_2.setText(filename)

    def functions(self):
        self.encrypt_btn.clicked.connect(lambda: self.encrypt(self.text_edit.toPlainText()))
        self.decrypt_btn.clicked.connect(lambda: self.decrypt(self.text_edit_encrypted.toPlainText()))

        self.key_btn.clicked.connect(lambda: self.open_key_file())
        self.OutputFile_btn.clicked.connect(lambda: self.change_output_files_labels('decrypt'))
        self.InputFile_btn.clicked.connect(lambda: self.change_input_files_labels('decrypt'))
        self.OutputFile_btn_2.clicked.connect(lambda: self.change_output_files_labels('encrypt'))
        self.InputFile_btn_2.clicked.connect(lambda: self.change_input_files_labels('encrypt'))

    def encrypt(self, text):
        key = ''
        # open input file
        if self.input_path_2.text() != 'NO INPUT FILE':
            fin = open('./txt/' + self.input_path_2.text(), 'r', encoding='UTF-8')
            text = fin.read()
            fin.close()

        # write generated key in key file
        if self.label_2.text() != 'NO KEY' and text != '':
            fout = open('./txt/' + self.label_2.text(), 'w', encoding='UTF-8')
            key = generate_key(len(text))
            fout.write(key)
            fout.close()

        # open key file
        if self.label_2.text() != 'NO KEY':
            fin = open('./txt/' + self.label_2.text(), 'r', encoding='UTF-8')
            key = fin.read()
            fin.close()

        encrypted_text = gamma(text, key)

        # open output file
        if self.output_path_2.text() != 'NO OUTPUT FILE':
            fout = open('./txt/' + self.output_path_2.text(), 'w', encoding='UTF-8')
            fout.write(encrypted_text)
            fout.close()
        else:
            self.textBrowser_encrypted.setText(encrypted_text)
        # self.decrypt(encrypted_text)

    def decrypt(self, text):
        key = ''
        # open key file
        if self.label_2.text() != 'NO KEY':
            fin = open('./txt/' + self.label_2.text(), 'r', encoding='UTF-8')
            key = fin.read()
            fin.close()

        # open input file
        if self.input_path.text() != 'NO INPUT FILE':
            fin = open('./txt/' + self.input_path.text(), 'r', encoding='UTF-8')
            text = fin.read()
            fin.close()

        decrypted_text = gamma(text, key)

        # open output file
        if self.output_path.text() != 'NO OUTPUT FILE':
            fout = open('./txt/' + self.input_path.text(), 'w', encoding='UTF-8')
            fout.write(decrypted_text)
            fout.close()
            self.textBrowser_decrypted.setPlainText(decrypted_text)
        else:
            self.textBrowser_decrypted.setText(decrypted_text)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Gamma()
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
