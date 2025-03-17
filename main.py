from math_utils.geometry import geometry_circle, geometry_rectangle
from math_utils.statistics import statistics_avg, statistics_med

user_list = list(map(int, input('Введите числа через пробел: ').split()))
print(user_list)

statistics_avg(user_list)
statistics_med(user_list)
geometry_circle(2)
geometry_rectangle(2, 3)
