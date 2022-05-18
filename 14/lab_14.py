from lab14_UI import *
from PyQt5.QtWidgets import QFileDialog
from os import path
import os.path
import Index_of_coincedence
import Autocorrelation
from Autocorrelation import drs, stic

# English lowercase
en_alph = list(map(chr, range(ord('a'), ord('z') + 1)))
# Russian lowercase
ru_alph = list(map(chr, range(ord('а'), ord('я') + 1)))
ru_alph.insert(6, 'ё')



def read_file(path: str):
    file = open(path, 'r', encoding='UTF-8')
    text = file.read()
    file.close()
    return text

class Analysis(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Analysis, self).__init__()
        self.setupUi(self)
        self.functions()
        self.method_comboBox.addItems(('Индекс совпадений', 'Автокорреляционный', 'Касиски'))
        self.language_comboBox.addItems(('RUS', 'ENG'))

    def change_interface(self):
        match self.method_comboBox.currentText():
            case 'Индекс совпадений':
                self.lang_name_2.setText('ВАРИАНТЫ\nКЛЮЧЕЙ')
                self.shift_count_spinbox.hide()
                self.shift_count_label.hide()
                # self.key_line.show()
                self.key_label.show()
                self.key_len_label.show()
                self.key_len_spinbox.show()
            case 'Автокорреляционный':
                self.lang_name_2.setText('ВОЗМОЖНЫЙ\nКЛЮЧ')
                self.shift_count_spinbox.show()
                self.shift_count_label.show()
                # self.key_line.show()
                self.key_label.show()
                self.key_len_label.hide()
                self.key_len_spinbox.hide()
            case 'Касиски':
                # self.key_line.show()
                self.key_label.show()
                self.key_len_label.show()
                self.key_len_spinbox.show()
                self.shift_count_spinbox.hide()
                self.shift_count_label.hide()

                self.lang_name_2.setText('ДЛИНЫ\nКЛЮЧА')

    def functions(self):
        self.method_comboBox.currentTextChanged.connect(lambda: self.change_interface())
        self.InputFile_btn.clicked.connect(lambda: self.change_file_label('in_file'))
        self.Open_InputFile_btn.clicked.connect(lambda: self.startToListen('in_file'))
        self.analize_btn.clicked.connect(lambda: self.analyze())

    def analyze(self):
        match self.language_comboBox.currentText():
            case 'RUS':
                alphabet = ru_alph
            case 'ENG':
                alphabet = en_alph
            case _:
                raise Exception('Wrong language!')
        input_text = read_file('./' + self.input_path.text())
        new_text = drs(input_text, alphabet)
        match self.method_comboBox.currentText():
            case 'Индекс совпадений':
                indicies = Index_of_coincedence.find_key_len(new_text, alphabet)
                self.graph(indicies)
                splitted_text = stic(new_text, self.key_len_spinbox.value())
            case 'Автокорреляционный':
                indicies = Autocorrelation.cac(new_text, self.shift_count_spinbox.value())
                self.graph(indicies)
            case 'Касиски':
                self.widget.clear()

    def startToListen(self, mode: str):
        file = ''
        match mode:
            case 'in_file':
                if self.input_path.text() != 'NO INPUT FILE':
                    file = os.path.abspath(self.input_path.text())
            case 'out_file':
                if self.output_path.text() != 'NO OUTPUT FILE':
                    file = os.path.abspath(self.output_path.text())
            case _:
                raise Exception('File name is empty')

        process = QtCore.QProcess(self)
        process.start('notepad', [file])

    def graph(self, dots):
        self.widget.clear()
        self.widget.setXRange(0, len(dots) - 1)
        x = []
        y = []
        for dot in dots:
            x.append(dot[0])
            y.append(dot[1])
        line = self.widget.plot(x, y)

    def open_file_dialog_box(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Open File', './')
        return path.basename(file)

    def change_file_label(self, type_of_file: str):
        filename = self.open_file_dialog_box()
        match type_of_file:
            case 'in_file':
                self.input_path.setText(filename)
                if not filename:
                    self.input_path.setText('NO INPUT FILE')
            case 'out_file':
                self.output_path.setText(filename)
                if not filename:
                    self.output_path.setText('NO OUTPUT FILE')
            case _:
                pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = Analysis()
    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


