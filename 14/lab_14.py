from lab14_UI import *
from PyQt5.QtWidgets import QFileDialog
from os import path
import os.path
from Vigenere import vigenere
import Index_of_coincedence
import Autocorrelation
from Autocorrelation import drs, stic, find_key_letter
import Kasiski

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


def ngrams_to_str(ngrams):
    result = ''
    for ngram in ngrams:
        result += f'{ngram[0]} : {ngram[1]}, '
    return result


class Analysis(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Analysis, self).__init__()
        self.setupUi(self)
        self.language_comboBox.addItems(('RUS', 'ENG'))
        self.method_comboBox.addItems(('Индекс совпадений', 'Автокорреляционный', 'Касиски'))
        self.labelOld = self.input_path.text()
        self._timer = QtCore.QTimer(self, interval=300)
        self._timer.timeout.connect(lambda: self.labelChanged())
        self._timer.start()

        self.shift_count_spinbox.hide()
        self.shift_count_label.hide()

        self.ngram_len_spinbox.hide()
        self.ngram_len_label.hide()

        self.key_len_combobox = QtWidgets.QComboBox(self.centralwidget)
        self.key_len_combobox.setGeometry(QtCore.QRect(350, 300, 91, 31))
        self.key_len_combobox.setStyleSheet("background-color: black;\n"
                                            "color: white;\n"
                                            "font-family: Century Gothic;\n"
                                            "font-size: 14px;")
        self.key_len_combobox.hide()

        self.functions()

    def labelChanged(self):
        if self.labelOld != self.input_path.text():
            self.labelOld = self.input_path.text()
            self.show_graph(self.language_comboBox.currentText())

    def change_interface(self):
        match self.method_comboBox.currentText():
            case 'Индекс совпадений':
                self.shift_count_spinbox.hide()
                self.shift_count_label.hide()
                self.lang_name_2.setText('ВАРИАНТЫ\nКЛЮЧЕЙ')
                # self.key_line.show()
                self.key_len_combobox.hide()
                self.key_label.show()
                self.key_len_label.show()
                self.key_len_spinbox.show()
                self.ngram_len_spinbox.hide()
                self.ngram_len_label.hide()
            case 'Автокорреляционный':
                self.lang_name_2.setText('ВОЗМОЖНЫЙ\nКЛЮЧ')
                self.shift_count_spinbox.show()
                self.shift_count_label.show()
                # self.key_line.show()
                self.key_len_combobox.hide()
                self.key_label.show()
                self.key_len_label.show()
                self.key_len_spinbox.show()
                self.ngram_len_spinbox.hide()
                self.ngram_len_label.hide()
            case 'Касиски':
                # self.key_line.show()
                self.key_label.show()
                self.key_len_label.show()
                self.key_len_spinbox.show()
                self.shift_count_spinbox.hide()
                self.shift_count_label.hide()

                self.widget.clear()
                self.key_len_spinbox.hide()
                self.key_len_combobox.show()
                self.ngram_len_label.show()
                self.ngram_len_spinbox.show()
                self.lang_name_2.setText('ПОПУЛЯРНЫЕ\nN-ГРАММЫ')

    def functions(self):
        self.method_comboBox.currentTextChanged.connect(lambda: self.change_interface())
        self.InputFile_btn.clicked.connect(lambda: self.change_file_label('in_file'))
        self.Open_InputFile_btn.clicked.connect(lambda: self.startToListen('in_file'))
        self.analize_btn.clicked.connect(lambda: self.analyze())
        self.method_comboBox.currentTextChanged.connect(lambda: self.show_graph(self.language_comboBox.currentText()))
        self.decrypt_btn.clicked.connect(lambda: self.decrypt(read_file('./' + self.input_path.text()),
                                                              self.key_combobox.currentText()))

    # def find_key_kasiski(self, text):
    #     strings = stic(text, int(self.key_len_combobox.currentText()))
    #     key = ''
    #     for string in strings:
    #         key += find_key_letter(string, self.language_comboBox.currentText())
    #     self.key_combobox.addItem(key)

    def show_graph(self, language):
        match language:
            case 'RUS':
                alphabet = ru_alph
            case 'ENG':
                alphabet = en_alph
            case _:
                raise Exception('Wrong language!')
        if self.input_path.text() != 'NO INPUT FILE':
            input_text = read_file('./' + self.input_path.text())
        else:
            input_text = ''
            self.widget.clear()
        new_text = drs(input_text, alphabet)
        match self.method_comboBox.currentText():
            case 'Индекс совпадений':
                indicies = Index_of_coincedence.find_key_len(new_text, alphabet)
                self.graph(indicies)
            case 'Автокорреляционный':
                indicies = Autocorrelation.cac(new_text, self.shift_count_spinbox.value())
                self.graph(indicies)
            case 'Касиски':
                self.widget.clear()

    def analyze(self):
        match self.language_comboBox.currentText():
            case 'RUS':
                alphabet = ru_alph
            case 'ENG':
                alphabet = en_alph
            case _:
                raise Exception('Wrong language!')
        if self.input_path.text() != 'NO INPUT FILE':
            input_text = read_file('./' + self.input_path.text())
        else:
            input_text = ''
        new_text = drs(input_text, alphabet)
        match self.method_comboBox.currentText():
            case 'Индекс совпадений':

                splitted_text = stic(new_text, self.key_len_spinbox.value())
                keys = Index_of_coincedence.find_keys(splitted_text, alphabet)
                self.key_combobox.clear()
                for key in keys:
                    self.key_combobox.addItem(key)

            case 'Автокорреляционный':
                self.key_combobox.clear()
                strings = stic(new_text, self.key_len_spinbox.value())
                key = ''
                for string in strings:
                    key += find_key_letter(string, self.language_comboBox.currentText())
                self.key_combobox.addItem(key)

            case 'Касиски':
                self.key_combobox.clear()
                ngram_list = Kasiski.find_ngramm(new_text, (self.ngram_len_spinbox.value()))
                self.textBrowser.setText(ngrams_to_str(ngram_list[:10]))
                key_length_options = Kasiski.find_key_length(ngram_list)
                if self.key_len_combobox.currentText() == '':
                    for option in key_length_options:
                        self.key_len_combobox.addItem(str(option))
                column_count = int(self.key_len_combobox.currentText())
                if column_count:
                    strings = stic(new_text, column_count)
                    key = ''
                    for string in strings:
                        key += find_key_letter(string, self.language_comboBox.currentText())
                    self.key_combobox.addItem(key)

    def decrypt(self, text, key):
        decrypted_text = vigenere(text, key, mode='decrypt')
        self.textBrowser_2.setText(decrypted_text)

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


