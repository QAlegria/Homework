import math

def geometry_circle(param: float) -> float:
    square_g = math.pi * math.pow(param, 2)
    print(f'Площадь круга равна = {square_g}')
    return square_g

def geometry_rectangle(param_1: float, param_2: float) -> float:
    square_g = param_1 * param_2
    print(f'Площадь прямоугольника равна = {square_g}')
    return square_g