#!/usr/bin/env python
# -*- coding: utf8 -*-

"""
Wszystkie programy proszę zrealizować w postaci funkcji, bez interfejsu i walidacji danych.
-----------
odp:
zastosowałem jednak minimalną validację danych, dla przyzwoitości.
działanie pod:
(venv) wiks@ubuntu:~/Dokumenty/projects/zad_rekr$ python --version
Python 3.6.9
wymaga instalacji six:
pip install six
-----------
zad 2 zawiera błąd w przykładowej odpowiedzi
zad 3 przyjąłem od do włącznie
-----------
PyDev console: starting.
Python 3.6.9 (default, Nov  7 2019, 10:44:02)
[GCC 8.3.0] on linux
import zad_rekr
... print(zad_rekr.range_of_postal_codes('09-995', '10-010'))
... print(zad_rekr.missing_list([2,3,7,4,9], 10))
... print(zad_rekr.from_2_to_5dot5_step_0dot5_list_decimal_format_generate())
...
['09-996', '09-997', '09-998', '09-999', '10-000', '10-001', '10-002', '10-003', '10-004', '10-005', '10-006', '10-007', '10-008', '10-009']
([1, 5, 6, 8], 'w treści zadania jest błąd, przykładowa odpowiedź zawiera 10, którego nie powinno być, bo lista ma być do "n-1"')
[Decimal('2'), Decimal('2.5'), Decimal('3'), Decimal('3.5'), Decimal('4'), Decimal('4.5'), Decimal('5'), Decimal('5.5')]
"""

from six import string_types
from decimal import *

'''
import zad_rekr
print(zad_rekr.range_of_postal_codes('09-995', '10-010'))
print(zad_rekr.missing_list([2,3,7,4,9], 10))
print(zad_rekr.from_2_to_5dot5_step_0dot5_list_decimal_format_generate())
'''


def range_of_postal_codes(*argv):
    """
    ZADANIE 1. GENERATOR KODÓW POCZTOWYCH
    przyjmuje 2 stringi: "79-900" i "80-155" i zwraca listę kodów pomiędzy nimi
    :param argv:
    :return:
    """
    res = []
    message = None
    if argv and len(argv) >= 2:
        arg_inted = []
        for arg in argv:
            if isinstance(arg, string_types):
                arg_splitted = arg.split('-')
                # print(arg_splitted)
                if len(arg_splitted) != 2:
                    message = 'wprowadzony kod pocztowy ( "{0}" ) nie jest poprawny, ' \
                              'poprawny wygląda podobnie jak: 12-345 '.format(arg)
                else:
                    arg_inted.append(int(arg_splitted[0]) * 1000 + int(arg_splitted[1]))
            else:
                message = 'wprowadzone dane powinny być typu string'
        if not message and len(arg_inted) >= 2:
            downer_code = arg_inted[0]
            upper_code = arg_inted[1]
            if upper_code < downer_code:
                downer_code = arg_inted[1]
                upper_code = arg_inted[0]
            downer_code += 1
            while downer_code < upper_code:
                main = int(downer_code/1000)
                res.append('{0:02d}-{1:03d}'.format(main, downer_code - main * 1000))
                downer_code += 1
    else:
        message = 'proszę wprowadzić dwa kody pocztowe w postaci string'
    if message:
        return message
    return res


def missing_list(*argv):
    """
    ZADANIE 2. PODANA JEST LISTA ZAWIERAJĄCA ELEMENTY O WARTOŚCIACH 1-n.
        NAPISZ FUNKCJĘ KTÓRA SPRAWDZI JAKICH ELEMENTÓW BRAKUJE
    1-n = [1,2,3,4,5,...,10]
    np. n=10
    wejście: [2,3,7,4,9], 10
    wyjście: [1,5,6,8,10]
    :param argv:
    :return:
    """
    res = []
    message = None
    inp_list = None
    n = None
    if argv and len(argv) >= 2:
        inp_list = argv[0]
        n = argv[1]
        if not isinstance(argv[0], list):
            message = 'proszę wprowadzić jako pierwszą daną listę liczb'
        if not isinstance(argv[1], int):
            message = 'proszę wprowadzić jako drugą daną wartość całkowitą "n"'
    else:
        message = 'proszę wprowadzić listę liczb, oraz wartość całkowitą "n"'
    if not message:
        res = []
        current = 1
        while current < n:
            if current not in inp_list:
                res.append(current)
            current += 1
    add_info = 'w treści zadania jest błąd, przykładowa odpowiedź zawiera 10, którego nie powinno być, ' \
               'bo lista ma być do "n-1"'
    if message:
        return message
    return res, add_info


def from_2_to_5dot5_step_0dot5_list_decimal_format_generate():
    """
    ZADANIE 3. NALEŻY WYGENEROWAĆ LISTĘ LICZB OD 2 DO 5.5 ZE SKOKIEM CO 0.5, DANE WYNIKOWE MUSZĄ BYĆ TYPU DECIMAL
    :return:
    """
    res = []
    getcontext().prec = 1
    current = 2.0
    while current <= 5.5:
        res.append(Decimal(current))
        current += 0.5
    return res
