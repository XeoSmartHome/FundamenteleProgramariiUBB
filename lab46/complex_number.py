import math


class ComplexNumber:
    def __init__(self, real, imaginary):
        """
        :type real: int
        :type imaginary: int
        """
        self.real = real
        self.imaginary = imaginary

    @property
    def real(self):
        return self._real

    @real.setter
    def real(self, value):
        self._real = float(value)

    @property
    def imaginary(self):
        return self._imaginary

    @imaginary.setter
    def imaginary(self, value):
        self._imaginary = float(value)

    def __repr__(self):
        return f'({self._real} + {self._imaginary}i)'

    def __eq__(self, other):
        return self._real == other.real and self._imaginary == other.imaginary

    def __add__(self, other):
        return ComplexNumber(self._real + other.real, self._imaginary + other.imaginary)

    def __sub__(self, other):
        return ComplexNumber(self._real - other.real, self._imaginary - other.imaginary)

    def __mul__(self, other):
        return ComplexNumber(self._real * other.real - self._imaginary * other.imaginary, self._imaginary * other.real + self._real * other.imaginary)

    def abs(self):
        """
        This function return the absolute value of a number
        """
        return math.sqrt(self._real * self._real + self._imaginary * self._imaginary)


def test_complex_number_class():
    assert ComplexNumber(11, 22).real == 11
    assert ComplexNumber(33, 44).imaginary == 44
    assert ComplexNumber(1, 2) == ComplexNumber(1, 2)
    assert ComplexNumber(3, 4) + ComplexNumber(2, 5) == ComplexNumber(5, 9)
    assert ComplexNumber(3, 4).abs() == 5
    assert ComplexNumber(-8, -6).abs() == 10
    assert ComplexNumber(5, 2) - ComplexNumber(10, -4) == ComplexNumber(-5, 6)


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
