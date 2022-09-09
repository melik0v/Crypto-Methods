from typing import Generator
import datetime


def generate_key(length: int) -> bytearray:
    key = []
    j = 0
    # seed = randint(0, 10 ** 10)
    mytime = '2016-Aug-04 08:24:38'
    time_delta = datetime.datetime.now() - datetime.datetime.strptime(str(mytime), '%Y-%b-%d %H:%M:%S')
    seed = int(time_delta.total_seconds())
    for i in lcg(255, 1103515245, 12345, seed):
        key.append(chr(i))
        j += 1
        if j == length - 1:
            break
    return bytearray(''.join(key), encoding='UTF-8')


def lcg(modulus: int, a: int, c: int, seed: int) -> Generator[int, None, None]:
    """Linear congruential generator."""
    while True:
        seed = (a * seed + c) % modulus
        yield seed
