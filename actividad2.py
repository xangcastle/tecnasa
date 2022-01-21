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
    print('▦' * 50)
    print("ejercicio 1")
    data = []
    params_count = int(input("Ingresa la cantidad de numeros que quieres usar: \n"))
    while len(data) < params_count:
        try:
            data.append(int(input(f'Ingresa el numero numero {len(data) + 1}:\n')))
        except (TypeError, ValueError):
            print('Debes ingresar solo números')

    print(f'el valor minimo es {my_min(data)}')
    print(f'el valor maximo es {my_max(data)}')


# task1()


def task2():
    print('▦' * 50)
    print("ejercicio 2")
    e = 2.54
    l = None
    while not l:
        try:
            l = int(input('Ingresa el largo de uno de los lados del cuadrado en metros:\n'))
        except (TypeError, ValueError):
            print('Ingresa solo números')
    print(f'El perimetro en centimetros es {l * 4}')
    print(f'El area en pulgadas es {((l ** 2) * 100) / e}')


# task2()


def task3():
    print('▦' * 50)
    print("ejercicio 3")
    b, h = 0, 0
    while b == 0 or h == 0:
        try:
            b = int(input('Ingresa el valor en metros de la base del triangulo\n'))
            h = int(input('Ingresa el valor en metros de la altura del triangulo\n'))
        except (TypeError, ValueError):
            print("por favor ingresa solo números")
    print(f'El area en metros del triangulo es {(b * h) / 2}')


# task3()


def task4():
    b, h, a = 0, 0, 0
    while b <= 0 or h <= 0 or a <= 0:
        try:
            b = int(input('Ingresa el valor del primer lado del triangulo\n'))
            h = int(input('Ingresa el valor del segundo lado del triangulo\n'))
            a = int(input('Ingresa el valor en grados del ángulo que une ambos lados del triangulo\n'))
        except (TypeError, ValueError):
            print(f'Debes ingresar solo números positivos')

    print(f'El area en metros del triangulo es {(b * h * sin(a)) / 2}')
    print(f'Se está usando una escala en grados por compatibilidad con math module')


task4()


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


# task5()


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


# task6()





