import string
# Задача 1: Создайте класс StringUtils с методами:

# @staticmethod is_palindrome(word) — проверяет, является ли слово палиндромом.

# @classmethod get_most_common(cls, text) — возвращает самый частый символ в тексте.


class StringUtils:
    @staticmethod
    def is_polindrom(user_string: str) -> bool:
        low_str = user_string.lower()
        return low_str == low_str[::-1]


user_str = "Topot, shepot i telega"
translator = str.maketrans('', '', string.punctuation)

fixed_str = user_str.translate(translator)
list_of_str = fixed_str.split()
print(list_of_str)

list_of_pol = list(
    filter(lambda word: StringUtils.is_polindrom(word) == True, list_of_str))

print(list_of_pol)
