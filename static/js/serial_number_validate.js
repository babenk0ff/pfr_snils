'use strict';

document.getElementById('serial_number').addEventListener(
    'input', (event) => {
        let match = event.target.value.replace(/\D/g, '')
            .match(/(\d{0,3})(\d{0,3})(\d{0,3})(\d{0,2})/);
        event.target.value = !match[2] ? match[1] : match[1] +
            '-' + match[2] +
            (match[3] ? '-' + match[3] : '') +
            (match[4] ? ' ' + match[4] : '');
    });

document.getElementById('serial_number').addEventListener(
    'input', (event) => checkInput(event.target));

window.addEventListener('DOMContentLoaded', (event) => {
    const input = document.getElementById('serial_number');
    checkInput(input);
})

function checkInput(input_obj) {
    const form = document.querySelector('form');

    if (input_obj.value.length === 14) {
        const clearedNumber = input_obj.value.replace(/-|\s/g, '');
        if (!check_sum(clearedNumber)) {
            if (document.querySelector('.invalid') === null) {
                const invalid_item = document.createElement('div');
                invalid_item.classList.add('invalid');
                invalid_item.innerText = 'Введенный номер некорректен';
                form.insertAdjacentElement("beforeend", invalid_item);
            }
        }
    } else {
        const invalid_item = document.querySelector('.invalid');
        if (invalid_item !== null) {
            invalid_item.remove();
        }
    }
}

function check_sum(numString) {
    const checksum = numString.slice(9);
    let calculatedSum;

    let digitsSum = 0;
    numString.slice(0, 9).split('').reverse().forEach(
        (digit, index) => {
            digitsSum += +digit * (index + 1);
        });
    digitsSum %= 101;

    calculatedSum = digitsSum === 100 ? '00' : digitsSum.toString();

    return calculatedSum === checksum;
}
