import time
import struct
import random
import hashlib
from multiprocessing import Pool


def slow_calculate(value: int) -> int:
    """Some weird voodoo magic calculations"""
    time.sleep(random.randint(1, 3))
    data = hashlib.md5(str(value).encode()).digest()
    return sum(struct.unpack('<' + 'B' * len(data), data))


def main():
    if __name__ == '__main__':
        pool = Pool(processes=50)
        result = sum(pool.map(slow_calculate, range(500)))
        return result
