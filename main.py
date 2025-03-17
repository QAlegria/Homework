from math_utils.geometry import geometry_circle, geometry_rectangle
from math_utils.statistics import statistics_avg, statistics_med

user_list = list(map(int, input('Введите числа через пробел: ').split()))
print(user_list)

avg = statistics_avg(user_list)
med = statistics_med(user_list)
s_circle = geometry_circle(2)
s_rectangle = geometry_rectangle(2, 3)


print(f'Среднее арифметическое = {avg}')
print(f'Медиана = {med}')
print(f'Площадь круга равна = {s_circle}')
print(f'Площадь прямоугольника равна = {s_rectangle}')