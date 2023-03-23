from dataclasses import dataclass

from models import SerialNumber
from serial_number.checksum_validator import validate


@dataclass
class CheckResult:
    number: str
    result: str


def get_check_result(num: str) -> CheckResult:
    if validate(num):
        num_from_db = SerialNumber.query.filter(
            SerialNumber.number == num
        ).first()
        result = 'НАЙДЕН' if num_from_db else 'ОТСУТСТВУЕТ'
    else:
        result = 'НЕВЕРЕН'

    return CheckResult(number=num, result=result)
