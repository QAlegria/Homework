import os
import sys


# Задача 3. Контекстный менеджер:
#
# Напишите контекстный менеджер FileWriter,
# который открывает файл в режиме записи и автоматически добавляет в конец файла строку
# "Файл закрыт" при выходе из блока with.

class FileWriter:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename,"w", encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.file.write("\n Файл закрыт")
        finally:
            self.file.close()

with FileWriter("test.txt") as file:
    file.write("Hello!")

# Домашнее задание: Контекстный менеджер для временного перенаправления вывода в файл
# Задача:
# Создайте контекстный менеджер RedirectStdout, который перенаправляет вывод функции
# print() в файл на время выполнения блока with.
# После выхода из блока вывод должен восстановиться в стандартный поток (консоль).

class RedirectStdout:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
        self.original_stdout = sys.stdout

    def __enter__(self):
        self.file = open(self.filename, "w", encoding="utf-8")
        sys.stdout = self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            sys.stdout = self.original_stdout
        finally:
            self.file.close()
with RedirectStdout("test.txt"):
    print("1241")
    print("dfkepokeokpfepokeokfoekfo kkepo 3ko3k")

print("Этого не должно быть  файле")