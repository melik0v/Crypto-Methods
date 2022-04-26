from matplotlib import pyplot as plt


# frequency crypto analisys
# English lowercase
en_alph = list(map(chr, range(ord('a'), ord('z') + 1)))
# Russian lowercase
ru_alph = list(map(chr, range(ord('а'), ord('я') + 1)))
ru_alph.insert(6, 'ё')

letters_nominal_freqs = {}


def read_file(path: str):
    file = open(path, 'r', encoding='UTF-8')
    text = file.read()
    file.close()
    return text


def get_nominal_freqs(language: str):
    match language:
        case 'english':
            path = './eng_letter_table.txt'
        case 'russian':
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
    Calculate count of letters included in alphabet

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
    # print(letters_real_freqs)
    for i in text:
        for key in letters_real_freqs.keys():
            if i.upper() == key:
                letters_real_freqs[key] += 1

    for key in letters_real_freqs.keys():
        letters_real_freqs[key] /= text_len
        letters_real_freqs[key] = round(letters_real_freqs[key], 3)

    return letters_real_freqs


def decrypt(nominal_freqs: dict, real_freqs: dict, text: str, language: str):
    match language:
        case 'english':
            alphabet = en_alph
        case 'russian':
            alphabet = ru_alph
        case _:
            alphabet = ''
    # strings from the keys of dictionaries of nominal and real frequencies
    nominal_keys = ''
    real_keys = ''
    for nominal_key, real_key in zip(nominal_freqs.keys(), real_freqs.keys()):
        nominal_keys += nominal_key
        real_keys += real_key
    # print(nominal_keys)
    # print(real_keys)
    result = ''
    for i in text:
        if i.lower() in alphabet:
            result += nominal_keys[real_keys.index(i)]
        else:
            result += i
    return result


def graph(dictionary: dict):
    dictionary = sort(dictionary, 'key', 'asc')
    dictionary = dictionary.items()
    x = []
    y = []
    for i in dictionary:
        x.append(i[0])
        y.append(i[1])
    fig, ax = plt.subplots()
    ax.bar(x, y)
    ax.set_facecolor('black')
    fig.set_facecolor('floralwhite')
    plt.show()


def functions(language: str):
    """
    Interface for access to other functions

    :param language: string with name of language e.g. 'russian'
    :return:
    """

    match language:
        case 'russian':
            alphabet = ru_alph
            path = './input_rus.txt'
        case 'english':
            alphabet = en_alph
            path = './input_eng.txt'
        case _:
            return 0
    # get_nominal_freqs('english')
    # print(letters_nominal_freqs)
    # input_text = read_file()
    # print(sort(calculate_letter_real_freqs(input_text, 'english')))
    # print(decrypt(letters_nominal_freqs, sort(calculate_letter_real_freqs
    # (input_text, 'english')), input_text, 'english'))
    get_nominal_freqs(language)
    print(letters_nominal_freqs)
    input_text = read_file(path)
    print(sort(calculate_letter_real_freqs(input_text, alphabet), 'value', 'desc'))
    print(decrypt(letters_nominal_freqs, sort(calculate_letter_real_freqs(input_text, alphabet), 'value', 'desc'),
                  input_text, language))

    graph(calculate_letter_real_freqs(input_text, alphabet))
    letters_nominal_freqs.clear()


print('ENGLISH')
functions('english')
functions('russian')
