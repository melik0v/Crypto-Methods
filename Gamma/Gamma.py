from Gamma_UI import QtWidgets, Ui_MainWindow
from PyQt5.QtWidgets import QFileDialog
from os import path
from random import randint
from typing import Generator
from PyQt5.QtWidgets import QMessageBox
import datetime


class GammaError(Exception):
    pass


def generate_key(length: int) -> bytearray:
    key = []
    j = 0
    # seed = randint(0, 10 ** 10)
    mytime = '2016-Aug-04 08:24:38'
    time_delta = datetime.datetime.now() - datetime.datetime.strptime(str(mytime), '%Y-%b-%d %H:%M:%S')
    seed = int(time_delta.total_seconds())
    for i in lcg(4096, 1103515245, 12345, seed):
        key.append(chr(i))
        j += 1
        if j == length - 1:
            break
    return bytearray(''.join(key), encoding='UTF-8')


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

    text = bytearray(text)
    for i in range(len(text)):
        text[i] ^= key[i % len(key)]

    return text


def end_notification():
    notification = QMessageBox()
    notification.setWindowTitle('Уведомление')
    notification.setText('Завершено')
    notification.setStandardButtons(QMessageBox.Close)
    close_btn = notification.button(QMessageBox.Close)
    close_btn.setText('Закрыть')
    notification.exec_()


class Gamma(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Gamma, self).__init__()
        self.setupUi(self)
        self.functions()

    def open_file_dialog_box(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Open File', './')
        return path.basename(file)

    def change_file_label(self, type_of_file: str):
        filename = self.open_file_dialog_box()
        match type_of_file:
            case 'key_file':
                self.label_2.setText(filename)
            case 'in_file':
                self.input_path_2.setText(filename)
            case 'out_file':
                self.lineEdit.setText(filename)
            case _:
                pass

    def refresh_key(self):
        if self.input_path_2.text() != 'NO INPUT FILE' and self.label_2.text() != 'NO KEY':
            with open(self.input_path_2.text(), 'rb') as fin:
                text = fin.read()
                # text = bytearray(text)
                length = len(text)
        else:
            return 0
        with open(self.label_2.text(), 'wb') as key_file:
            key_file.write(generate_key(length))
        end_notification()

    def encrypt(self):
        text = ''
        if self.input_path_2.text() != 'NO INPUT FILE':
            with open(self.input_path_2.text(), 'rb') as fin:
                text = fin.read()
        if self.label_2.text() != 'NO KEY':
            # with open(self.label_2.text(), 'wb') as key_file:
            #     key_file.write(generate_key(len(text)))
            with open(self.label_2.text(), 'rb') as key_file:
                key = key_file.read()
        else:
            return 0
        encrypted_text = gamma(text, key)
        if self.lineEdit.text():
            with open(self.lineEdit.text(), 'wb') as fout:
                fout.write(encrypted_text)
        end_notification()

    def functions(self):
        self.encrypt_btn.clicked.connect(lambda: self.encrypt())
        self.refresh_key_btn.clicked.connect(lambda: self.refresh_key())
        self.InputFile_btn_2.clicked.connect(lambda: self.change_file_label('in_file'))
        self.OutputFile_btn_2.clicked.connect(lambda: self.change_file_label('out_file'))
        self.key_btn.clicked.connect(lambda: self.change_file_label('key_file'))



# with open('image.jpg', 'rb') as fin:
#     text = fin.read()
#
# with open('key.txt', 'wb') as key_file:
#     key_file.write(generate_key(len(text)))
#
# with open('key.txt', 'rb') as key_file:
#      key = key_file.read()
#
# encrypted_text = gamma(text, key)
#
# with open('test.txt', 'wb') as fout:
#     fout.write(encrypted_text)
#
# with open('test.txt', 'rb') as fin:
#     text = fin.read()
#
# decrypted_text = gamma(text, key)
#
# with open('output.txt', 'wb') as fout:
#     fout.write(decrypted_text)

