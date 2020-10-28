import math


def ComplexNumber(real, imaginary):
    return {
        'real': real,
        'imaginary': imaginary
    }


def add(self, other):
    return {
        'real': self['real'] + other['real'],
        'imaginary': self['imaginary'] + other['imaginary']
    }


def sub(self, other):
    return {
        'real': self['real'] - other['real'],
        'imaginary': self['imaginary'] - other['imaginary']
    }


def mul(self, other):
    return {
        'real': self['real'] * other['real'] - self['imaginary'] * other['imaginary'],
        'imaginary': self['imaginary'] * other['real'] + self['real'] * other['imaginary']
    }


def abs(self):
    """
        This function return the absolute value of a number
    """
    return math.sqrt(self['real'] * self['real'] + self['imaginary'] * self['imaginary'])


def test_complex_number_class():
    assert ComplexNumber(11, 22)['real'] == 11
    assert ComplexNumber(33, 44)['imaginary'] == 44
    assert ComplexNumber(1, 2) == ComplexNumber(1, 2)
    assert add(ComplexNumber(3, 4), ComplexNumber(2, 5)) == ComplexNumber(5, 9)
    assert abs(ComplexNumber(3, 4)) == 5
    assert abs(ComplexNumber(-8, -6)) == 10
    assert sub(ComplexNumber(5, 2), ComplexNumber(10, -4)) == ComplexNumber(-5, 6)


def is_prime(number):
    """
    This function check if a given number is prime or not
    :type number: int
    """
    number = int(number)

    if number < 2:
        return False
    if number < 4:
        return True
    if number % 2 == 0:
        return False
    for d in range(3, number // 2, 2):
        if number % d == 0:
            return False
    return True


def test_prime_function():
    assert not is_prime(-5)
    assert not is_prime(1)
    assert is_prime(2)
    assert is_prime(3)
    assert not is_prime(4)
    assert is_prime(5)
    assert is_prime(7)
    assert not is_prime(49)
