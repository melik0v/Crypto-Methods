from des_beta import DES
from os import path
from DES_UI import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox
from GOST.Gamma import generate_key


class Make(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(Make, self).__init__()
        self.setupUi(self)
        self.comboBox.addItems(('ECB', 'CFB', 'OFB', 'CBC'))
        self.init_vector_label.hide()
        self.iv_btn.hide()
        self.label_3.hide()
        self.refresh_iv_btn.hide()
        self.old_method_name = self.comboBox.currentText()
        # self._timer = QtCore.QTimer(self, interval=500)
        # self._timer.timeout.connect(lambda: self.method_changed())
        self.functions()

    def open_file_dialog_box(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Open File', './')
        return path.basename(file)

    def change_file_label(self, type_of_file: str):
        filename = self.open_file_dialog_box()
        match type_of_file:
            case 'key_file':
                if not filename:
                    self.label_2.setText('NO KEY')
                    return
                self.label_2.setText(filename)
            case 'in_file':
                if not filename:
                    self.input_path_2.setText('NO INPUT FILE')
                    return
                self.input_path_2.setText(filename)
            case 'out_file':
                if not filename:
                    self.input_path_2.setText('NO INPUT FILE')
                    return
                self.lineEdit.setText(filename)
            case 'iv_file':
                if not filename:
                    self.label_3.setText('NO INIT VECTOR')
                    return
                self.label_3.setText(filename)
            case _:
                pass

    def functions(self):
        self.comboBox.currentTextChanged.connect(lambda: self.change_interface())
        self.InputFile_btn_2.clicked.connect(lambda: self.change_file_label('in_file'))
        self.key_btn.clicked.connect(lambda: self.change_file_label('key_file'))
        self.OutputFile_btn_2.clicked.connect(lambda: self.change_file_label('out_file'))
        self.iv_btn.clicked.connect(lambda: self.change_file_label('iv_file'))
        self.refresh_key_btn.clicked.connect(lambda: self.refresh_key())
        self.encrypt_btn.clicked.connect(lambda: self.make('enc'))
        self.decrypt_btn.clicked.connect(lambda: self.make('dec'))
        self.refresh_iv_btn.clicked.connect(lambda: self.refresh_iv())

    def make(self, mode: str):
        encrypted_text = ''
        if self.input_path_2.text() != 'NO INPUT FILE':
            with open('./' + self.input_path_2.text(), 'rb') as file:
                input_text = file.read()

        if self.label_2.text() != 'NO KEY':
            with open(self.label_2.text(), 'rb') as key_file:
                key = key_file.read()

        if self.label_3.text() != 'NO INIT VECTOR':
            with open(self.label_3.text(), 'rb') as file:
                iv = file.read()

        a = DES()

        match mode:
            case 'enc':
                match self.comboBox.currentText():
                    case 'ECB':
                        encrypted_text = a.ECB(input_text, key, mode='enc')
                    case 'CFB':
                        encrypted_text = a.CFB(input_text, key, iv, mode='enc')
                    case 'CBC':
                        encrypted_text = a.CBC(input_text, key, iv, mode='enc')
                    case 'OFB':
                        encrypted_text = a.OFB(input_text, key, iv, mode='enc')
                    case _:
                        raise Exception("Wrong mode!")

            case 'dec':
                match self.comboBox.currentText():
                    case 'ECB':
                        encrypted_text = a.ECB(input_text, key, mode='dec')
                    case 'CFB':
                        encrypted_text = a.CFB(input_text, key, iv, mode='dec')
                    case 'CBC':
                        encrypted_text = a.CBC(input_text, key, iv, mode='dec')
                    case 'OFB':
                        encrypted_text = a.OFB(input_text, key, iv, mode='dec')
                    case _:
                        raise Exception("Wrong mode!")
        if self.lineEdit.text():
            with open(self.lineEdit.text(), 'wb') as fout:
                fout.write(encrypted_text)
        else:
            return

        end_notification()

    def change_interface(self):
        match self.comboBox.currentText():
            case "ECB":
                self.init_vector_label.hide()
                self.iv_btn.hide()
                self.refresh_iv_btn.hide()
                self.label_3.hide()
            case "CFB":
                self.init_vector_label.show()
                self.refresh_iv_btn.show()
                self.iv_btn.show()
                self.label_3.show()

    def refresh_key(self):
        with open(self.label_2.text(), 'wb') as key_file:
            key_file.write(generate_key(32))
        end_notification()

    def refresh_iv(self):
        with open(self.label_3.text(), 'wb') as iv_file:
            iv_file.write(generate_key(8))
        end_notification()


def end_notification():
    notification = QMessageBox()
    notification.setWindowTitle('Уведомление')
    notification.setText('Завершено')
    notification.setStandardButtons(QMessageBox.Close)
    close_btn = notification.button(QMessageBox.Close)
    close_btn.setText('Закрыть')
    notification.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Make()
    MainWindow.show()
    sys.exit(app.exec_())
