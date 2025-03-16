# Создайте пакет math_utils с модулями:
#
# geometry.py (функции для площади круга и прямоугольника).
#
# statistics.py (функции для среднего значения и медианы списка).
#
# Напишите main.py, который импортирует и использует эти функции.

import math

def geometry_circle(param):
    square_g = math.pi * math.pow(param, 2)
    print(f'Площадь круга равна = {square_g}')
    return square_g

def geometry_rectangle(param_1, param_2):
    square_g = param_1 * param_2
    print(f'Площадь прямоугольника равна = {square_g}')
    return square_g

def statistics_avg(param_list):
    avg = sum(param_list)/(len(param_list))
    print(f'Среднее арифметическое = {avg}')
    return avg

def statistics_med(param_list):
    list.sort(param_list)
    len_list = len(param_list)
    if len_list % 2 == 0:
        med = (param_list[(len_list//2)-1] + param_list[len_list//2]) / 2
    else:
        med = param_list[len_list//2]
    print(f'Медиана = {med}')
    return med