from Caesar import caesar
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


def stic(text: str, column_length: int) -> tuple:
    """
    Split text into columns with length <column_length>.

    """
    strings = ['' for _ in range(column_length)]
    for i in range(len(text)):
        strings[i % column_length] += text[i]
    return tuple(strings)


def read_file(path: str):
    file = open(path, 'r', encoding='UTF-8')
    text = file.read()
    file.close()
    return text


def ioc(string: str, alphabet: list) -> float:
    """
    Calculate index of coincedence.

    """
    result = 0
    string = string.lower()
    length = len(string)
    for letter in alphabet:
        tmp = string.count(letter)
        result += (tmp * (tmp - 1)) / (length * (length - 1))
    return result


def mioc(string_1: str, string_2: str, alphabet: list) -> float:
    """
    Calculate mutual index of coincedence between two strings.

    """
    result = 0
    string_1 = string_1.lower()
    string_2 = string_2.lower()
    len_1 = len(string_1)
    len_2 = len(string_2)
    for letter in alphabet:
        tmp = (string_1.count(letter) * string_2.count(letter)) / (len_1 * len_2)
        result += tmp
    return result


def decrypt(text, key):
    return vigenere(text, key, mode='decrypt')


def find_key_len(text: str, alphabet: list, length: int):
    """
    Find length of keyword.

    """
    max_len = len(text) // 2
    if length > max_len:
        length = max_len
    text = drs(text, alphabet)
    indicies_arithmetic_mean = []
    tmp = 0
    for i in range(1, length):
        strings = stic(text, i)
        for string in strings:
            tmp += ioc(string, alphabet)
        tmp /= len(strings)
        indicies_arithmetic_mean.append((i, tmp))
    # print(indicies_arithmetic_mean)
    return indicies_arithmetic_mean


def find_keys(strings: tuple[str], alphabet: list) -> tuple:
    """
    Find all of <power of alphabet> possible keys

    """
    indicies = []
    keys = []
    for i in range(1, len(strings)):
        mutual_index = 0.0
        shift = 0
        for j in range(1, len(alphabet)):
            tmp = mioc(strings[0], caesar(strings[i], j), alphabet)
            if mutual_index < tmp:
                mutual_index = tmp
                shift = j
        indicies.append((mutual_index, shift))
    # print(np.array(indicies))
    for letter in alphabet:
        key_word = letter
        for index in indicies:
            key_word += alphabet[alphabet.index(letter) - index[1]]
        keys.append(key_word)
    return tuple(keys)


# input_text = read_file('./input_eng_2.txt')
# find_key_len(input_text, en_alph)
# splitted_text = stic(drs(input_text, en_alph), 5)
# print(np.array(splitted_text))
# print("IOC")
# for substr in splitted_text:
#     print(ioc(substr, en_alph))
# print("MIOC")
# print(np.array(find_keys(splitted_text, en_alph)))
# print(decrypt(input_text, 'hello'))

