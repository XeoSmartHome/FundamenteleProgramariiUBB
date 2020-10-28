import math
from lab46_v2.complex_number import ComplexNumber, test_complex_number_class, test_prime_function, abs, add, sub, mul
from lab46_v2.complex_number_list import ComplexNumberList, test_complex_number_list_class, test_remove_primes_numbers
from lab46_v2.console import Console


complex_number_list = ComplexNumberList()


def add(params: list):
    if len(params) == 2:
        r = int(params[0])
        i = int(params[1])
    else:
        r = int(input("real_part = "))
        i = int(input("imaginary_part = "))
    complex_number_list.append(ComplexNumber(r, i))


def insert(params: list):
    r = int(input("real_part = "))
    i = int(input("imaginary_part = "))
    position = int(input("position = "))
    complex_number_list.insert(ComplexNumber(r, i), position)


def print_imaginary_part_of_sublist(params: list):
    start = int(input('start = '))
    stop = int(input('stop = '))
    for number in complex_number_list.numbers()[start: stop]:
        print(number['imaginary'])


def print_numbers_with_abs_smaller_than_10(params: list):
    for number in complex_number_list.numbers():
        if abs(number) < 10:
            print(number)


def print_number_with_abs_equal_10(params: list):
    for number in complex_number_list.numbers():
        if abs(number) == 10:
            print(number)


def sum_of_sublist(params: list):
    start = int(input('start = '))
    stop = int(input('stop = '))
    print(complex_number_list.sum(start, stop))


def product_of_sublist(params: list):
    start = int(input('start = '))
    stop = int(input('stop = '))
    print(complex_number_list.product(start, stop))


def print_desc_imaginary(params: list):
    for number in sorted(complex_number_list.numbers(), key=lambda x: -x['imaginary']):
        print(number)


def undo(params: list):
    complex_number_list.undo()
    print('Undo done')


def remove_primes(params: list):
    complex_number_list.remove_primes()
    print('prime numbers removed')


def print_list(params: list):
    print(complex_number_list.numbers())


def remove_abs(params: list):
    number = int(input('number = '))
    condition = input('condition = ')
    if condition == '<':
        complex_number_list.delete_with_filter(lambda x: abs(x) < number)
    elif condition == '>':
        complex_number_list.delete_with_filter(lambda x: abs(x) > number)
    elif condition == '=' or condition == '==':
        complex_number_list.delete_with_filter(lambda x: abs(x) == number)
    else:
        print('condition not found')


def remove_element(params: list):
    number_index = int(input('remove element from index i = '))
    complex_number_list.delete(number_index)
    print('Number removed')


def remove_interval(params: list):
    start_index = int(input('start_index = '))
    stop_index = int(input('stop index = '))
    complex_number_list.delete_sublist(start_index, stop_index)


def replace(params: list):
    number_r = int(input('number real part = '))
    number_i = int(input('number imaginary part = '))
    replace_with_r = int(input('replace with real part = '))
    replace_with_i = int(input('replace with part = '))
    complex_number_list.replace(ComplexNumber(number_r, number_i), ComplexNumber(replace_with_r, replace_with_i))


def test_all():
    test_complex_number_class()
    test_complex_number_list_class()
    test_prime_function()
    test_remove_primes_numbers()


console = Console()
console.register_function('add', add, 'add a complex number at the end of the list')
console.register_function('insert', insert, 'insert a complex number at a given position')
console.register_function('list', print_list, 'list all numbers')
console.register_function('imaginary', print_imaginary_part_of_sublist, 'print imaginary part of specific sublist')
console.register_function('abs<10', print_numbers_with_abs_smaller_than_10, 'print all numbers with abs smaller than 10')
console.register_function('abs==10', print_number_with_abs_equal_10, 'print all numbers with abs equal 10')
console.register_function('sum', sum_of_sublist, 'calculate the sum of a specific sublist')
console.register_function('product', product_of_sublist, 'calculate the sum of a specific sublist')
console.register_function('desc_imaginary', print_desc_imaginary, 'print numbers sorted desc by imaginary part')
console.register_function('remove_primes', remove_primes, 'remove numbers with prime real part')
console.register_function('remove_abs', remove_abs, 'remove all number that are </>/= with a given number')
console.register_function('remove', remove_element, 'remove an element from a given position')
console.register_function('replace', replace, 'replace a number with another number')
console.register_function('undo', undo, 'undo last operation')

test_all()
console.start()
