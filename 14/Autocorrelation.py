import numpy as np
from Vigenere import vigenere
from Caesar import caesar


# English lowercase
en_alph = list(map(chr, range(ord('a'), ord('z') + 1)))
# Russian lowercase
ru_alph = list(map(chr, range(ord('а'), ord('я') + 1)))
ru_alph.insert(6, 'ё')


def get_nominal_freqs(language: str) -> dict:
    letters_nominal_freqs = {}
    match language:
        case 'ENG':
            path = './eng_letter_table.txt'
        case 'RUS':
            path = './rus_letter_table.txt'
        case _:
            path = './eng_letter_table.txt'
    with open(path, encoding='UTF-8') as file:
        for line in file:
            key, value = line.split()
            letters_nominal_freqs[key] = float(value)
    return letters_nominal_freqs


def calculate_letter_real_freqs(text: str, expected_freqs: dict) -> dict:
    text_len = len(text)
    letters_real_freqs = {key: 0 for key in expected_freqs.keys()}
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


def stic(text: str, column_length: int) -> tuple:
    """
    Split text into columns with length <column_length>.

    """
    strings = ['' for _ in range(column_length)]
    for i in range(len(text)):
        strings[i % column_length] += text[i]
    return tuple(strings)


def drs(text: str, alphabet: list):
    """
    Delete redundant symbols from text.

    """
    result = ''
    for i in text:
        if i.isalpha() and i.lower() in alphabet:
            result += i
    return result


# def roll(string: str, shift: int):
#     new_string = string[-shift:-1]
#     new_string += string[-1]
#     new_string += string[:-shift]
#     return new_string[:-shift]


def cac(string: str, shifts: int) -> list[tuple]:
    """
    Calculate autocorrelation coefficients

    """
    autocorrelation_coefficiets = []
    for i in range(1, min(shifts, len(string) - 1)):
        coincedence_count = 0
        rolled_string = string[i:]
        for j in range(1, len(rolled_string) - i):
            if string[j] == rolled_string[j]:
                coincedence_count += 1
        coefficient = coincedence_count / (len(string) - i)
        autocorrelation_coefficiets.append((i, coefficient))
    return autocorrelation_coefficiets


def pierson_criteria(expected: tuple, observed: tuple) -> float:
    result = 0
    for i in range(len(expected)):
        result += ((observed[i] - expected[i]) ** 2) / expected[i]
    return result


def get_values(dictionary: dict) -> tuple:
    """
    Get values from dictionary with the preservation of order

    :return: Tuple of values
    """
    result = []
    for item in dictionary.items():
        result.append(item[1])
    return tuple(result)


def find_key_letter(text: str, language: str) -> str:
    """
    Find letter of the key

    :return: letter of the key
    """
    match language:
        case 'RUS':
            alphabet = ru_alph
        case 'ENG':
            alphabet = en_alph
        case _:
            raise Exception('Wrong language!')
    nominal_freqs = get_nominal_freqs(language)
    # print(nominal_freqs)
    results = []
    for i in range(len(alphabet)):
        shifted_text = caesar(text, i)
        real_freqs = calculate_letter_real_freqs(shifted_text, nominal_freqs)
        # print(f'{i} : {real_freqs}')
        results.append(pierson_criteria(get_values(nominal_freqs), get_values(real_freqs)))
    # print(np.array(results))
    shift = (len(alphabet) - results.index(min(results))) % len(alphabet)
    return alphabet[shift]


def read_file(path: str):
    file = open(path, 'r', encoding='UTF-8')
    text = file.read()
    file.close()
    return text


# input_text = read_file('./input_eng_2.txt')
# print(cac(drs(input_text, en_alph), 50))
# strings = stic(drs(input_text, en_alph), 5)
# key = ''
# for string in strings:
#     key += find_key_letter(string, 'ENG')
# print(key)
# print(vigenere(input_text, key, mode='decrypt'))
