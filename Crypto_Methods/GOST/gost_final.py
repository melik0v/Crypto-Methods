import time
import os
import bitarray
from bitarray.util import ba2int, int2ba
from Gamma import generate_key


S = ((0xF, 0xC, 0x2, 0xA, 0x6, 0x4, 0x5, 0x0, 0x7, 0x9, 0xE, 0xD, 0x1, 0xB, 0x8, 0x3),
     (0xB, 0x6, 0x3, 0x4, 0xC, 0xF, 0xE, 0x2, 0x7, 0xD, 0x8, 0x0, 0x5, 0xA, 0x9, 0x1),
     (0x1, 0xC, 0xB, 0x0, 0xF, 0xE, 0x6, 0x5, 0xA, 0xD, 0x4, 0x8, 0x9, 0x3, 0x7, 0x2),
     (0x1, 0x5, 0xE, 0xC, 0xA, 0x7, 0x0, 0xD, 0x6, 0x2, 0xB, 0x4, 0x9, 0x3, 0xF, 0x8),
     (0x0, 0xC, 0x8, 0x9, 0xD, 0x2, 0xA, 0xB, 0x7, 0x3, 0x6, 0x5, 0x4, 0xE, 0xF, 0x1),
     (0x8, 0x0, 0xF, 0x3, 0x2, 0x5, 0xE, 0xB, 0x1, 0xA, 0x4, 0x7, 0xC, 0x9, 0xD, 0x6),
     (0x3, 0x0, 0x6, 0xF, 0x1, 0xE, 0x9, 0x2, 0xD, 0x8, 0xC, 0x4, 0xB, 0xA, 0x5, 0x7),
     (0x1, 0xA, 0x6, 0x8, 0xF, 0xB, 0x0, 0x4, 0xC, 0x3, 0x5, 0x9, 0x7, 0xD, 0x2, 0xE))


class GOST:

    def encrypt(self, text, key):
        return self.__enc_dec(text, key, 'enc')

    def decrypt(self, text, key):
        return self.__enc_dec(text, key, 'dec')

    def __enc_dec(self, text, key, mode):
        keys = self.__generate_keys(key)

        l_half, r_half = text[:32], text[32:]

        key_indecies = list(range(8)) * 3 + list(range(7, -1, -1))
        rounds_indecies = range(32)

        if mode == 'dec':
            rounds_indecies = reversed(rounds_indecies)

        for round_index in rounds_indecies:
            l_half, r_half = self.__func_F(l_half, keys[key_indecies[round_index]], round_index) ^ r_half, l_half

        return r_half + l_half

    @staticmethod
    def __generate_keys(key):
        keys = []
        for i in range(0, 256, 32):
            keys.append(key[i:i + 32])

        return keys

    @staticmethod
    def __func_F(N2, key, round):
        text = int2ba((ba2int(N2) + ba2int(key)) % 2 ** 32, length=32)

        text_S = bitarray.bitarray()
        for i in range(0, 32, 4):
            text_S += int2ba(S[round % 8][ba2int(text[i:i + 4])], length=4)

        return text_S[11:] + text_S[:11]

    def ECB(self, text, key, mode):
        text = self.__expand_text_len(text)
        key = self.__expand_key_len(key)

        text_bin = self.__text_to_bin(text)
        key_bin = self.__key_to_bin(key)

        enc_dec_text = []

        if mode == 'enc':
            for i in range(0, len(text_bin), 64):
                # enc_dec_text.append(self.encrypt(text_bin[i:i + 64], key_bin).tobytes().decode('koi8-r'))
                enc_dec_text.append(self.encrypt(text_bin[i:i + 64], key_bin).tobytes())

        if mode == 'dec':
            for i in range(0, len(text_bin), 64):
                # enc_dec_text.append(self.decrypt(text_bin[i:i + 64], key_bin).tobytes().decode('koi8-r'))
                enc_dec_text.append(self.decrypt(text_bin[i:i + 64], key_bin).tobytes())

        result = bytes()
        for block in enc_dec_text:
            result += block

        return result

    def CFB(self, text, key, init_vect_text, mode):
        text = self.__expand_text_len(text)
        key = self.__expand_key_len(key)
        init_vect_text = self.__expand_key_len(init_vect_text)

        text_bin = self.__text_to_bin(text)
        key_bin = self.__key_to_bin(key)
        vect = self.__init_vect_to_bin(init_vect_text)

        enc_dec_text = []

        if mode == 'enc':
            for i in range(0, len(text_bin), 64):
                vect = self.encrypt(vect, key_bin) ^ text_bin[i:i + 64]
                # enc_dec_text.append(vect.tobytes().decode('koi8-r'))
                enc_dec_text.append(vect.tobytes())

        if mode == 'dec':
            for i in range(0, len(text_bin), 64):
                # enc_dec_text.append((self.encrypt(vect, key_bin) ^ text_bin[i:i + 64]).tobytes().decode('koi8-r'))
                enc_dec_text.append((self.encrypt(vect, key_bin) ^ text_bin[i:i + 64]).tobytes())
                vect = text_bin[i:i + 64]

        result = bytes()
        for block in enc_dec_text:
            result += block

        return result

    @staticmethod
    def __expand_text_len(text):
        if len(text) % 8 != 0:
            text += bytes(b'\x00') * (8 - len(text) % 8)

        return text

    @staticmethod
    def __expand_key_len(key):
        if len(key) == 0:
            return 'sample text'

        if len(key) % 32 != 0 and type(key) == str:
            key += ' ' * (32 - len(key) % 32)

        return key

    @staticmethod
    def __text_to_bin(text):
        text_bin = bitarray.bitarray()
        text_bin.frombytes(text)

        return text_bin

    @staticmethod
    def __key_to_bin(key):
        key_bin = bitarray.bitarray()
        key_bin.frombytes(key[:32])
        # key_bin.frombytes(key[:32].encode('koi8-r', errors='replace'))
        # key_bin.frombytes(key.encode('UTF-8'))
        return key_bin

    @staticmethod
    def __init_vect_to_bin(init_vect):
        init_vect_bin = bitarray.bitarray()
        # init_vect_bin.frombytes(init_vect[:8].encode('koi8-r'))
        init_vect_bin.frombytes(init_vect[:8])

        return init_vect_bin


# filename = 'big_file.pdf'
# with open(filename, 'rb') as file:
#     input_text = file.read()
# print(f'Размер файла {os.stat(os.path.abspath(filename)).st_size} байт')
# with open('key.txt', 'rb') as file:
#     key = file.read()
# start_time = time.time()
# a = GOST()
# output_text = a.ECB(input_text, key, mode='enc')
# iv = bytes(generate_key(8))[:8]
# # output_text = b'\00'
# # output_text = a.CFB(input_text, key, iv, mode='enc')
# # print(output_text)
# print(f'Файл зашифрован за {time.time() - start_time} сек')
# start_time = time.time()
# decrypted_text = a.ECB(output_text, key, mode='dec')
# # decrypted_text = a.CFB(output_text, key, iv, mode='dec')
# print(f'Файл расшифрован за {time.time() - start_time} сек')
#
# with open('decrypted', 'wb') as file:
#     file.write(decrypted_text)

# print(decrypted_text)
