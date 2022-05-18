import numpy as np
from Autocorrelation import stic, find_key_letter
from Vigenere import vigenere

# English lowercase
en_alph = list(map(chr, range(ord('a'), ord('z') + 1)))
# Russian lowercase
ru_alph = list(map(chr, range(ord('а'), ord('я') + 1)))
ru_alph.insert(6, 'ё')


def drs(text: str, alphabet: list):
    """
    Delete redundant symbols from text.

    """
    result = ''
    for i in text:
        if i.isalpha() and i.lower() in alphabet:
            result += i
    return result


def read_file(path: str):
    file = open(path, 'r', encoding='UTF-8')
    text = file.read()
    file.close()
    return text


def sort(ngrams: list, mode: str):
    for i in range(len(ngrams)):
        for j in range(i, len(ngrams)):
            if len(ngrams[i][1]) < len(ngrams[j][1]):
                tmp = ngrams[i]
                ngrams[i] = ngrams[j]
                ngrams[j] = tmp

    match mode:
        case 'asc':
            ngrams.reverse()
        case 'desc':
            pass
    return ngrams


def find_ngramm(text: str, length: int) -> tuple:
    """
    Find number of repetitions of the ngram in the text
    :param text: analyzed text
    :param length: length of n-gram
    :return: tuple of most popular n-grams
    """
    text_len = len(text)
    result = []
    for i in range(text_len - text_len % length):
        ngram = text[i:length + i:]
        indicies = []
        for j in range(text_len - text_len % length):
            tmp = text[j:length + j:]
            if tmp == ngram:
                indicies.append(j + 1)
        if len(indicies) > 1:
            tmp = (ngram, tuple(indicies))
            if tmp not in result:
                result.append(tmp)
    # print(ngram)

    # print(result)
    # print(sort(result, 'desc'))
    # print(sort(result, 'asc'))
    return tuple(sort(result, 'desc'))


def calc_distance(ngram: tuple) -> tuple:
    distances = []
    for i in range(1, len(ngram)):
        distances.append(ngram[i] - ngram[i - 1])
    return tuple(distances)


def gcd(numbers: tuple) -> int:
    """
    Great common divisor between multiple numbers.

    :param numbers: tuple of numbers
    """
    result = np.gcd(numbers[0], numbers[1])
    for i in range(2, len(numbers)):
        result = np.gcd(result, numbers[i])
    return result


def find_key_length(ngrams) -> tuple:
    ngrams = ngrams[:10]
    possible_len_list = []
    for ngram in ngrams:
        distances = calc_distance(ngram[1])
        possible_len_list.append(gcd(distances))

    # print(ngrams)
    # print(possible_len_list)
    # print(distances)
    # print(gcd(distances))
    return tuple(set(possible_len_list))


input_text = read_file('./input_rus_2.txt')
ngram_list = find_ngramm(drs(input_text, ru_alph), 3)
key_length_options = find_key_length(ngram_list)
print(f'Возможные длины ключа: {key_length_options}')

strings = stic(drs(input_text, ru_alph), key_length_options[1])
key = ''
for string in strings:
    key += find_key_letter(string, 'RUS')
print(f'Ключ: {key}')
print(vigenere(input_text, key, mode='decrypt'))
