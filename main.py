import math_utils

user_list = list(map(int, input('Введите числа через пробел: ').split()))
print(user_list)

math_utils.statistics_avg(user_list)
math_utils.statistics_med(user_list)
math_utils.geometry_circle(2)
math_utils.geometry_rectangle(2, 3)
