from .complex_number import ComplexNumber, is_prime


class ComplexNumberList:
    def __init__(self):
        self._list = []
        self._list_backup = []

    def _backup(self):
        self._list_backup.append([element for element in self._list])

    def append(self, complex_number):
        """
        This function add a number at the end of the list
        :type complex_number: ComplexNumber
        :return: None
        """
        self._backup()
        self._list.append(complex_number)

    def insert(self, complex_number, index):
        """
        This function insert a number at a given position
        :type complex_number: ComplexNumber
        :type index: int
        :return: None
        """
        self._backup()
        self._list.insert(index, complex_number)

    def delete(self, index):
        """
        This function delete a number from a given position
        :type index: int
        :return: None
        """
        self._backup()
        self._list.pop(index)

    def delete_sublist(self, start_index, stop_index):
        """
        This function delete a sublist, from start_index to stop_index
        :type start_index: int
        :type stop_index: int
        :return: None
        """
        self._backup()
        for index in range(start_index, stop_index):
            self._list.pop(index)

    def replace(self, old_complex_number, new_complex_number):
        """
        This function replace a number with another number everywhere it appears
        :type old_complex_number: ComplexNumber
        :type new_complex_number: ComplexNumber
        :return: None
        """
        self._backup()
        for index in range(len(self._list)):
            if self._list[index] == old_complex_number:
                self._list[index] = new_complex_number

    def undo(self):
        """
        undo last list operation
        """
        l = len(self._list_backup)
        if l > 0:
            self._list = self._list_backup.pop(l-1)

    def numbers(self):
        """
        return the list of all numbers
        """
        return self._list

    def sum(self, start=0, stop=None):
        """
        This function calculate the sum of a sublist
        """
        if stop is None:
            stop = len(self._list)
        s = ComplexNumber(0, 0)
        for number in self._list[start: stop+1]:
            s += number
        return s

    def product(self, start=0, stop=None):
        """
        This function calculate the sum of a sublist
        """
        if stop is None:
            stop = len(self._list)
        p = ComplexNumber(1, 0)
        for number in self._list[start: stop + 1]:
            p *= number
        return p

    def delete_with_filter(self, filter_function):
        """
        This function delete elements that match the filter
        """
        self._backup()
        self._list = list(filter(lambda x: not filter_function(x), self._list))

    def select_with_filter(self, filter_function):
        """
        This function return all elements that match the filter
        """
        return list((filter(filter_function, self._list)))

    def remove_primes(self):
        """
        This function remove numbers with prime real part
        """
        self.delete_with_filter(lambda x: is_prime(x.real))


def test_remove_primes_numbers():
    test_list = ComplexNumberList()
    test_list.append(ComplexNumber(5, 2))
    test_list.append(ComplexNumber(-10, 4))
    test_list.remove_primes()
    assert test_list.numbers()[0] == ComplexNumber(-10, 4)
    test_list.append(ComplexNumber(6, 8))
    test_list.append(ComplexNumber(17, 9))
    test_list.append(ComplexNumber(200, 300))
    test_list.remove_primes()
    assert test_list.numbers()[2] == ComplexNumber(200, 300)


def test_complex_number_list_class():
    test_remove_primes_numbers()
