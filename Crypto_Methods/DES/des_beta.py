from tables import *
import os
import bitarray
from bitarray.util import ba2int, int2ba
import time


class DES:
    def encrypt(self, text, key):
        return self.__enc_dec(text, key, 'enc')

    def decrypt(self, text, key):
        return self.__enc_dec(text, key, 'dec')

    def __enc_dec(self, text, key, mode):
        keys = self.__key_expansion(key)
        text_ip = self.__permutate(text, 64, IP)

        N1, N2 = text_ip[:32], text_ip[32:]

        indexes = range(16) if mode == 'enc' else range(15, -1, -1)

        for round in indexes:
            N1, N2 = N2, self.__func_F(N2, keys[round]) ^ N1

        return self.__permutate(N2 + N1, 0, IP_INV)

    def __permutate(self, block, length: int, table: tuple):
        result = ""
        for i in table:
            result += str(block[i - 1])
        return bitarray.bitarray(result)

    def __add_redundant_bits(self, block: bitarray.bitarray) -> bitarray.bitarray:
        result = bitarray.bitarray()
        for i in range(0, 56, 7):
            tmp = block[i: i + 7]
            if tmp.count(1) % 2 == 0:
                tmp.append(1)
            else:
                tmp.append(0)
            result += tmp
        return result

    def __key_expansion(self, key):
        key = self.__add_redundant_bits(key)
        key_pc1 = bitarray.bitarray(self.__permutate(key, 56, KEY_P_TABLE))

        key_left = key_pc1[:28]
        key_right = key_pc1[28:]

        keys_left_shifted = []
        keys_right_shifted = []
        for shift in SHIFTS:
            key_left = key_left[shift:] + key_left[:shift]
            keys_left_shifted.append(key_left)

            key_right = key_right[shift:] + key_right[:shift]
            keys_right_shifted.append(key_right)

        keys_pc2 = []
        for i in range(16):
            left_right = keys_left_shifted[i] + keys_right_shifted[i]

            tmp = bitarray.bitarray(self.__permutate(left_right, 56, KEY_P_2_TABLE))

            keys_pc2.append(tmp)

        return keys_pc2

    @staticmethod
    def __substitutions(res):
        res_s = bitarray.bitarray()
        for i in range(0, 48, 6):
            row = ba2int(bitarray.bitarray([res[i], res[i + 5]]))
            col = ba2int(res[i + 1:i + 5])

            res_s += int2ba(S[i // 6][(row * col)], length=4)

        return res_s

    def __func_F(self, N2, key):
        # R_expansed = self.__expansion_permutation(N2)
        R_expansed = self.__permutate(N2, 0, E)
        res = key ^ R_expansed
        res_s = self.__substitutions(res)
        # res_s_f = self.__permutation(res_s)
        res_s_f = self.__permutate(res_s, 0, P)

        return res_s_f

    def ECB(self, text, key, mode):
        text = self.expand_text_len(text)
        # key = self.expand_key_len(key)

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

    def CBC(self, text, key, init_vect_text, mode):
        text = self.expand_text_len(text)
        # key = self.expand_key_len(key)
        # init_vect_text = self.expand_key_len(init_vect_text)

        text_bin = self.__text_to_bin(text)
        key_bin = self.__key_to_bin(key)
        vect = self.__init_vect_to_bin(init_vect_text)

        enc_dec_text = []

        if mode == 'enc':
            for i in range(0, len(text_bin), 64):
                vect = self.encrypt(text_bin[i:i + 64] ^ vect, key_bin)
                enc_dec_text.append(vect.tobytes())
                # enc_dec_text.append(vect.tobytes().decode('koi8-r'))

        if mode == 'dec':
            for i in range(0, len(text_bin), 64):
                # enc_dec_text.append((vect ^ self.decrypt(text_bin[i:i + 64], key_bin)).tobytes().decode('koi8-r'))
                enc_dec_text.append((vect ^ self.decrypt(text_bin[i:i + 64], key_bin)).tobytes())
                vect = text_bin[i:i + 64]

        result = bytes()
        for block in enc_dec_text:
            result += block

        return result

    def CFB(self, text, key, init_vect_text, mode):
        text = self.expand_text_len(text)
        # key = self.expand_key_len(key)
        # init_vect_text = self.expand_key_len(init_vect_text)

        text_bin = self.__text_to_bin(text)
        key_bin = self.__key_to_bin(key)
        vect = self.__init_vect_to_bin(init_vect_text)

        enc_dec_text = []

        if mode == 'enc':
            for i in range(0, len(text_bin), 64):
                vect = self.encrypt(vect, key_bin) ^ text_bin[i:i + 64]
                enc_dec_text.append(vect.tobytes())
                # enc_dec_text.append(vect.tobytes().decode('koi8-r'))

        if mode == 'dec':
            for i in range(0, len(text_bin), 64):
                # enc_dec_text.append((self.encrypt(vect, key_bin) ^ text_bin[i:i + 64]).tobytes().decode('koi8-r'))
                enc_dec_text.append((self.encrypt(vect, key_bin) ^ text_bin[i:i + 64]).tobytes())
                vect = text_bin[i:i + 64]

        result = bytes()
        for block in enc_dec_text:
            result += block

        return result

    def OFB(self, text, key, init_vect_text, mode):
        text = self.expand_text_len(text)
        # key = self.expand_key_len(key)
        # init_vect_text = self.expand_key_len(init_vect_text)

        text_bin = self.__text_to_bin(text)
        key_bin = self.__key_to_bin(key)
        vect = self.__init_vect_to_bin(init_vect_text)

        enc_dec_text = []

        if mode == 'enc':
            for i in range(0, len(text_bin), 64):
                vect = self.encrypt(vect, key_bin)
                enc_dec_text.append((vect ^ text_bin[i:i + 64]).tobytes())
                # enc_dec_text.append((vect ^ text_bin[i:i + 64]).tobytes().decode('koi8-r'))

        if mode == 'dec':
            for i in range(0, len(text_bin), 64):
                vect = self.encrypt(vect, key_bin)
                enc_dec_text.append((vect ^ text_bin[i:i + 64]).tobytes())
                # enc_dec_text.append((vect ^ text_bin[i:i + 64]).tobytes().decode('koi8-r'))

        result = bytes()
        for block in enc_dec_text:
            result += block

        return result

    def expand_text_len(self, text):
        if len(text) % 8 != 0:
            text += bytes(b'\x00') * (8 - len(text) % 8)

        return text

    def expand_init_vect_len(self, init_vect):
        if len(init_vect) == 0:
            return 'vector?'

        if len(init_vect) % 8 != 0:
            init_vect += ' ' * (8 - len(init_vect) % 8)

        return init_vect

    def __text_to_bin(self, text):
        text_bin = bitarray.bitarray()
        # text_bin.frombytes(text.encode('koi8-r'))
        text_bin.frombytes(text)

        return text_bin

    def __key_to_bin(self, key):
        key_bin = bitarray.bitarray()
        # key_bin.frombytes(key[:7].encode('koi8-r'))
        key_bin.frombytes(key[:8])

        return key_bin

    def __init_vect_to_bin(self, init_vect):
        init_vect_bin = bitarray.bitarray()
        # init_vect_bin.frombytes(init_vect[:8].encode('koi8-r'))
        init_vect_bin.frombytes(init_vect[:8])

        return init_vect_bin


# a = DES()
# filename = 'video.mp4'
# with open(filename, 'rb') as file:
#     input_text = file.read()
# iv = 'vector?!'
# print(f'Размер файла {os.stat(os.path.abspath(filename)).st_size} байт')
# key = bytes('_hello_', encoding='koi8-r')
# start_time = time.time()
# output_text = a.ECB(input_text, key, mode='enc')
# # output_text = a.CFB(input_text, key, iv, mode='enc')
# # output_text = a.CBC(input_text, key, iv, mode='enc')
# # output_text = a.OFB(input_text, key, iv, mode='enc')
# print(f'Файл зашифрован за {time.time() - start_time} сек')
#
# start_time = time.time()
# decrypted_text = a.ECB(output_text, key, mode='dec')
# # decrypted_text = a.CFB(output_text, key, iv, mode='dec')
# # decrypted_text = a.CBC(output_text, key, iv, mode='dec')
# # decrypted_text = a.OFB(output_text, key, iv, mode='dec')
# print(f'Файл расшифрован за {time.time() - start_time} сек')
#
# with open('decrypted.mp4', 'wb') as file:
#     file.write(decrypted_text)

