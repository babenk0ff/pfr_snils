import re


def calc_checksum(num_string: str) -> str:
    digits_sum = 0
    for i, digit in enumerate(num_string[::-1]):
        digits_sum += int(digit) * (i + 1)

    digits_sum = digits_sum % 101

    if digits_sum == 100:
        return '00'
    if digits_sum < 10:
        return '0' + str(digits_sum)
    return str(digits_sum)


def validate(number: str):
    pattern = r'^\d{3}-\d{3}-\d{3}\s\d{2}$'
    if re.fullmatch(pattern, re.sub(r'\n|\r', '', number)):
        checksum = number[-2:]
        number_only = number[:-2].strip().replace('-', '')
        return checksum == calc_checksum(number_only)
    return False
