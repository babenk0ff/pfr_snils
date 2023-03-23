'use strict';

const numberInput = document.getElementById('serial_number');
const numberForm = document.querySelector('.form_serial_number');

// Слушатель событий на поле ввода номера, реализующий
// маску вида "ХХХ-ХХХ-ХХХ ХХ"
numberInput.addEventListener(
    'input', (event) => {
        let match = event.target.value.replace(/\D/g, '')
            .match(/(\d{0,3})(\d{0,3})(\d{0,3})(\d{0,2})/);
        event.target.value = !match[2] ? match[1] : match[1] +
            '-' + match[2] +
            (match[3] ? '-' + match[3] : '') +
            (match[4] ? ' ' + match[4] : '');
    });

// Слушатель событий для запуска валидации при вводе номера
numberInput.addEventListener(
    'input', (event) => {
        if (event.value.length === 14 && !validNumber(numberInput.value)) {
            setFeedback(false)
        } else {
            setFeedback(true)
        }
    });

// Слушатель событий, добавляющий предупреждение о невалидности номера после
// загрузки страницы
window.addEventListener('DOMContentLoaded', () => {
    if (numberInput.value.length === 14 && !validNumber(numberInput.value)) {
        setFeedback(false)
    }
});

// Слушатель событий, предотвращающий отправку формы с невалидным номером
numberForm.addEventListener('submit', (event) => {
    if (!validNumber(numberInput.value)) {
        event.preventDefault();
        setFeedback(false)
    }
});

/**
 * Проверяет СНИЛС на валидность
 * @param num - СНИЛС
 * @returns {boolean} возвращает результат проверки
 */
function validNumber(num) {
    const reGex = /\d{3}-\d{3}-\d{3}\s\d{2}/
    return reGex.test(num) && ifChecksumValid(num);
}

/**
 * Добавляет или удаляет соответствующее валидности СНИЛС предупреждение
 * под полем ввода. Проверяется только полностью введенный номер (длина строки
 * равна 14).
 * @param {(false|true)} state - валидность номера
 */
function setFeedback(state) {
    const invalid_item = document.querySelector('.invalid');
    if (!state) {
        if (invalid_item === null) {
            const invalid_item = document.createElement('div');
            invalid_item.classList.add('invalid');
            invalid_item.innerText = 'Введенный номер некорректен';
            numberForm.insertAdjacentElement("beforeend", invalid_item);
        }
    } else {
        if (invalid_item !== null) invalid_item.remove()
    }
}

/**
 * Для полученного СНИЛС вычисляет контрольную сумму и сравнивает с имеющейся.
 * @param {string} raw_number - строка, представляющая собой СНИЛС
 * @returns {boolean} возвращает результат сравнения вычисленной
 * контрольной суммы с имеющейся
 */
function ifChecksumValid(raw_number) {
    const clearedNumber = raw_number.replace(/-|\s/g, '');
    const checksum = clearedNumber.slice(9);
    let calculatedSum;

    let digitsSum = 0;
    clearedNumber.slice(0, 9).split('').reverse().forEach(
        (digit, index) => {
            digitsSum += +digit * (index + 1);
        });
    digitsSum %= 101;

    calculatedSum = digitsSum === 100 ? '00' : digitsSum.toString();
    console.log(calculatedSum)
    return calculatedSum === checksum;
}
