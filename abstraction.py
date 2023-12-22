# Мой первый commit

from abc import ABC, abstractmethod

class Book(ABC):
    '''Класс использющий абстрактный метод get_summary'''
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def get_summary(self):
        pass

class Fiction(Book):
    def get_summary(self):
        print(f'"{self.title}" - роман в стиле исторический фикшн, автор - {self.author}')

class NonFiction(Book):
    def get_summary(self):
        print(f'"{self.title}" - книга в стиле нон фикшн, автор - {self.author}')

class Poetry(Book):
    pass
