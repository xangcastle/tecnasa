from math import sin


class Point:

    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __str__(self):
        return f'{self.x}, {self.y}'

    def distance(self, p2):
        return ((self.x - p2.x) ** 2) + ((self.y - p2.y) ** 2) ** 0.5


def my_min(data):
    x = data[0]
    for y in data:
        if y < x:
            x = y
    return x


def my_max(data):
    x = data[0]
    for y in data:
        if y > x:
            x = y
    return x


def task1():
    data = []
    params_count = int(input("Please type the qty of numbers that you want to use: \n"))
    for p in range(0, params_count):
        data.append(input(f'Please type the param {p + 1}'))

    print(f'the min value is {my_min(data)}')
    print(f'the max value is {my_max(data)}')


def task2():
    e = 2.54
    l = 3
    print(f'El perimetro en centimetros es {l * 4}')
    print(f'El area en pulgadas es {((l ** 2) * 100) / e}')


def task3():
    try:
        b = int(input('Ingresa el valor en metros de la base del triangulo\n'))
        h = int(input('Ingresa el valor en metros de la altura del triangulo\n'))
        if b > 0 and h > 0:
            print(f'El area en metros del triangulo es {(b * h) / 2}')

    except TypeError:
        print("por favor ingresa solo números")


def task4():
    try:
        b = int(input('Ingresa el valor en metros de la base del triangulo\n'))
        h = int(input('Ingresa el valor en metros de la altura del triangulo\n'))
        a = int(input('Ingresa el valor en grados del ángulo que une ambos lados del triangulo\n'))
        if a > 0 and b > 0 and h > 0:
            print(f'El area en metros del triangulo es {b * h * sin(a)}')
            print(f'Se está usando una escala en grados por compatibilidad con math module')
        print(f'Debes ingresar solo números positivos')
    except (TypeError, ValueError):
        print("por favor ingresa solo números")


def task5():
    data = []
    while len(data) < 10:
        try:
            x = int(f'Por favor ingresa el dato número {len(data) + 1}')
            if x > 0:
                data.append(x)
        except (ValueError, TypeError):
            pass

    a = data[0]
    b = data[1]
    da = abs(a - b)
    for n, i in enumerate(data):
        if n > 1:
            dd = abs(a - data[n])
            if dd < da:
                b = data[n]

    print(f'El número mas cercano al {a} es {b}')


def task6():
    points = []

    def define_point(n):
        x, y = input(f'Ingresa el punto número {n} ejemplo: 3,4 \n').split(',')
        return Point(x, y)

    for c in range(0, 5):
        points.append(define_point(c))

    p1 = points.pop(0)
    p2 = points[0]
    d = p1.distance(p2)
    points = [{
        'point': p,
        'distance': p.distance(p1)
    } for p in points]

    for punto in points:
        if punto.get('distance') < d:
            d = punto.get('distance')
            p2 = punto.get('point')

    print(f'el punto mas cercano a {p1} es {p2}')








