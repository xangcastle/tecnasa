from math import sin, cos, pi
import termplotlib as tpl
from skimage.draw import polygon2mask


class Point:

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return f'({self.x}, {self.y})'

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


task1()


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


task2()


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


task3()


def task4():
    print('▦' * 50)
    print("ejercicio 4")
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
    print('▦' * 50)
    print("ejercicio 5")
    data = []
    while len(data) < 10:
        try:
            x = int(input(f'Por favor ingresa el dato número {len(data) + 1}:\n'))
            if x > 0:
                data.append(x)
            print('por favor ingresa solo números positivos')
        except (ValueError, TypeError):
            print('por favor ingresa solo números positivos')

    a = data[0]
    b = data[1]
    da = abs(a - b)
    for n, i in enumerate(data):
        if n > 1:
            dd = abs(a - data[n])
            if dd < da:
                b = data[n]

    print(f'El número mas cercano al {a} es {b}')


task5()


def task6():
    print('▦' * 50)
    print("ejercicio 6")
    points = []

    def define_point(n):
        x, y = input(f'Ingresa el punto número {n} ejemplo: 3,4 \n').split(',')
        return Point(x, y)

    while len(points) < 5:
        try:
            points.append(define_point(len(points) + 1))
        except (ValueError, TypeError):
            print('Favor ingresa las coordenadas del punto separadas por una coma')

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


task6()


def task7():
    print('▦' * 50)
    print("ejercicio 7")
    n, m = 0, 0
    while n <= 0 or m <= 0:
        try:
            n = int(input('Ingresa en número n:\n'))
            m = int(input('Ingresa en número m:\n'))
        except (TypeError, ValueError):
            print('Ingresa solo números positivos')

    data = [num for num in range(n, int(n * m) + 1, n)]

    print(data)


task7()


def task8():
    print('▦' * 50)
    print("ejercicio 8")


def task9():
    print('▦' * 50)
    print("ejercicio 9")
    height, width, slides = 0, 0, 0
    while height == 0 and width == 0 and slides == 0:
        try:
            height = int(input("Ingresa el alto: \n"))
            width = int(input("Ingresa el ancho: \n"))
            slides = int(input("Ingresa la cantidad de lados: \n"))
        except (TypeError, ValueError):
            print("Error. Ingresa solo números positivos")

    shape = (width * 4, height * 4)

    def make_polygon(sides, radius=1, translation=None):
        segment = pi * 2 / sides
        coords = [(sin(segment * i) * radius, cos(segment * i) * radius)
                  for i in range(sides)]
        if translation:
            coords = [[sum(pair) for pair in zip(point, translation)]
                      for point in coords]
        return coords

    points = make_polygon(slides, int((height + width) // 2), translation=(int(width * 1.5), int(height * 1.5)))

    img = polygon2mask(shape, points).astype(str)
    img[img == "True"] = "*"
    img[img == "False"] = " "
    print(img)
    for row in img:
        print("".join(row))


task9()


def task10():
    print('▦' * 50)
    print("ejercicio 10")
    number = None
    domain, results = [], []

    def sequence(n):
        data = list()
        while n != 1:
            data.append(n)
            if n % 2 == 0:
                n = n // 2
            else:
                n = (3 * n) + 1
        data.append(1)
        return len(data)

    while not number:
        try:
            number = int(input("Ingresa un número entero\n"))
            domain = list(range(1, number + 1))
            results = [sequence(x) for x in domain]
        except (TypeError, ValueError):
            pass

    fig = tpl.figure()
    fig.barh(results, domain, force_ascii=True)
    fig.show()


task10()
