import pandas as pd

from lab79.books.book import Book

book = Book('aaa', 'bbb', 'ccc')

dict1 = [book]

df = pd.DataFrame(data=dict1, index=[0])

df.to_excel('dict1.xlsx')


students_grades = pd.read_excel('dict1.xlsx')

a = students_grades.to_dict()

print(a)
