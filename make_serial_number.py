import random
from textwrap import wrap

number = '123456789'


def calc_checksum(string: str) -> str:
    result = 0
    for i, digit in enumerate(string[::-1]):
        result += int(digit) * (i + 1)

    result = result % 101
    if result == 100:
        return '00'
    if result < 10:
        return '0' + str(result)
    return str(result)


def get_snils(amount):
    result = []
    for _ in range(amount):
        num = ''.join([str(random.randint(0, 9)) for _ in range(9)])
        result.append(f'{"-".join(wrap(num, 3))} {calc_checksum(num)}')
    return result


for n in get_snils(10):
    print(n)

print(get_snils(10))
