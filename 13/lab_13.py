import os.path

import numpy
from os import path
import pyqtgraph
from matplotlib import pyplot as plt
from Caesar import caesar
from lab13_UI import QtWidgets, Ui_MainWindow, PlotWidget
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore


# frequency crypto analisys
# English lowercase
en_alph = list(map(chr, range(ord('a'), ord('z') + 1)))
# Russian lowercase
ru_alph = list(map(chr, range(ord('а'), ord('я') + 1)))
ru_alph.insert(6, 'ё')

letters_nominal_freqs = {}


class FreqAnalisys(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(FreqAnalisys, self).__init__()
        self.setupUi(self)
        # grid = QtWidgets.QGridLayout(self.widget)
        # grid.addWidget(self.widget, 0, 0)
        self.functions()

    def functions(self):
        self.decrypt_btn.clicked.connect(lambda: self.analize(self.comboBox.currentText()))
        self.InputFile_btn.clicked.connect(lambda: self.change_file_label('in_file'))
        self.OutputFile_btn.clicked.connect(lambda: self.change_file_label('out_file'))
        self.Open_InputFile_btn.clicked.connect(lambda: self.startToListen('in_file'))
        self.Open_OutputFile_btn.clicked.connect(lambda: self.startToListen('out_file'))

    def open_file_dialog_box(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Open File', './')
        return path.basename(file)

    def change_file_label(self, type_of_file: str):
        filename = self.open_file_dialog_box()
        match type_of_file:
            case 'in_file':
                self.input_path.setText(filename)
            case 'out_file':
                self.output_path.setText(filename)
            case _:
                pass

    def analize(self, language: str):
        """
        Interface for access to other functions

        :param language: string with name of language e.g. 'russian'
        :return:
        """

        match language:
            case 'RUS':
                alphabet = ru_alph
            case 'ENG':
                alphabet = en_alph
            case _:
                return 0

        self.widget.clear()
        get_nominal_freqs(language)
        print(letters_nominal_freqs)

        input_text = read_file('./' + self.input_path.text())
        sorted_real_freqs = sort(calculate_letter_real_freqs(input_text, alphabet), 'value', 'desc')
        print(sorted_real_freqs)
        decrypted_text = (decrypt(letters_nominal_freqs, sorted_real_freqs, input_text, language))
        self.make_gistogram(letters_nominal_freqs, sorted_real_freqs)
        self.textBrowser.setText(decrypted_text)
        if self.output_path.text() != 'NO OUTPUT FILE':
            with open('./' + self.output_path.text(), 'w', encoding='UTF-8') as fout:
                fout.write(decrypted_text)
        letters_nominal_freqs.clear()

    def startToListen(self, mode: str):
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

        # self.setEnabled(False)
        # process.finished.connect(lambda: self.setEnabled(True))

    def make_gistogram(self, freqs_nominal: dict, freqs_real: dict):
        freqs_real = sort(freqs_real, 'key', 'asc')
        ticks = [list(zip(range(len(freqs_real) + 1), freqs_real.keys()))]
        freqs_real = freqs_real.items()

        freqs_nominal = sort(freqs_nominal, 'key', 'asc')
        freqs_nominal = freqs_nominal.items()

        letter_real = []
        letter_nominal = []
        freq_real = []
        freq_nominal = []
        c = 0
        for i, j in zip(freqs_real, freqs_nominal):
            letter_nominal.append(c - 0.1)
            letter_real.append(c + 0.1)

            freq_real.append(i[1])
            freq_nominal.append(j[1])
            c += 1

        self.widget.setYRange(0, max(freq_nominal) * 1.005, 0.05)
        xax = self.widget.getAxis('bottom')
        xax.setTicks(ticks)
        bargraph_nominal = pyqtgraph.BarGraphItem(x=letter_nominal, height=freq_nominal, brush='blue', width=0.2)
        bargraph_real = pyqtgraph.BarGraphItem(x=letter_real, height=freq_real, brush='red', width=0.2)
        self.widget.addItem(bargraph_real)
        self.widget.addItem(bargraph_nominal)


def read_file(path: str):
    file = open(path, 'r', encoding='UTF-8')
    text = file.read()
    file.close()
    return text


def get_nominal_freqs(language: str):
    match language:
        case 'ENG':
            path = './eng_letter_table.txt'
        case 'RUS':
            path = './rus_letter_table.txt'
        case _:
            return 0
    with open(path, encoding='UTF-8') as file:
        for line in file:
            key, value = line.split()
            letters_nominal_freqs[key] = float(value)


def sort(dictionary: dict, field: str, order: str) -> dict:
    """
    Sort dictionary in descending order

    :param dictionary: Dictionary to be sorted
    :param field: field which dictionary is sorted (key or value)
    :param order: descending or ascending order (des or asc)
    :return: Sorted dictionary
    """
    match field:
        case 'key':
            sorted_tuple = sorted(dictionary.items(), key=lambda x: x[0])
        case 'value':
            sorted_tuple = sorted(dictionary.items(), key=lambda x: x[1])
        case _:
            sorted_tuple = sorted(dictionary.items(), key=lambda x: x[0])
    match order:
        case 'asc':
            pass
        case 'desc':
            sorted_tuple.reverse()
        case _:
            pass

    return dict(sorted_tuple)


def clc(text: str, alphabet) -> int:
    """
    Calculate count of letters in text included in alphabet

    :param text: Text to be checked
    :param alphabet: Charset
    :return: Numbers of letters
    """
    result = 0
    for i in text:
        if i.lower() in alphabet:
            result += 1
    return result



def calculate_letter_real_freqs(text: str, alphabet) -> dict:
    text_len = clc(text, alphabet)
    letters_real_freqs = {key: 0 for key in letters_nominal_freqs.keys()}
    for i in text:
        for key in letters_real_freqs.keys():
            if i.upper() == key:
                letters_real_freqs[key] += 1

    for key in letters_real_freqs.keys():
        try:
            letters_real_freqs[key] /= text_len
        except ZeroDivisionError:
            letters_real_freqs[key] = 0
        letters_real_freqs[key] = round(letters_real_freqs[key], 3)

    return letters_real_freqs


def decrypt(nominal_freqs: dict, real_freqs: dict, text: str, language: str):
    match language:
        case 'ENG':
            alphabet = en_alph
        case 'RUS':
            alphabet = ru_alph
        case _:
            alphabet = ''
    # strings from the keys of dictionaries of nominal and real frequencies
    nominal_keys = ''
    real_keys = ''
    for nominal_key, real_key in zip(nominal_freqs.keys(), real_freqs.keys()):
        nominal_keys += nominal_key
        real_keys += real_key

    shift = alphabet.index(nominal_keys[0].lower()) - alphabet.index(real_keys[0].lower())
    result = caesar(text, shift)
    # for i in text:
    #     if i.lower() in alphabet:
    #         result += nominal_keys[real_keys.index(i.upper())]
    #     else:
    #         result += i
    return result
