# -*- coding: utf-8 -*-
from dialog import Dialog
import click
from datetime import datetime
import time
import math
import webbrowser
import enum

d = Dialog(dialog="dialog")
d.set_background_title("Curso Python - Cesar Abel")


def terminate():
    d.infobox("Adios...", width=0, height=0, title="Vuelve pronto")
    time.sleep(1)
    return 0


def make_form(data, title="", description=""):
    fields = [(i, n + 1, 2, data[i], n + 1, 25, 25, 25) for n, i in enumerate(data)]
    return d.form(description, fields, 0, 0, 0, title=title)


def task1():
    return make_form({
        "Nombres": "",
        "Apellidos": "",
    },
        title="Ejercicio 1",
        description="Escriba un programa que solicite el nombre y apellido del usuario por "
                    "separado y luego presente un mensaje de bienvenida al mismo de forma "
                    "concatenada agregando la fecha y hora.")


def task2():
    return make_form({
        "Numero 1": "",
        "Numero 2": "",
        "Numero 3": "",
        "Numero 4": "",
        "Numero 5": "",
    },
        title="Ejercicio 2",
        description="Escriba un programa que solicite cinco numeros, multiplique los primeros "
                    "tres y luego restele el cuarto numero y finalmente sumele el ultimo numero "
                    "elevado al cubo, el mensaje de sálida debera de lucir de la siguiente "
                    "manera: La respuesta al problema es:[R]")


def task3():
    r = math.sqrt(16 + 5) + math.pi * (5 / 2) * math.pow(3, 7)
    return d.msgbox(f'Implementar\nr = √16 + 5 + pi ∗ (+5/2) ∗ 3!\n\nResult: {"{:.2f}".format(r)}',
                    width=40,
                    title='Ejercicio 3')


def task4():
    r = math.factorial(9) - 16 ** (1 / 4)
    return d.msgbox(f'Implementar\nr = 9! − ∜16\n\nResult: {"{:.2f}".format(r)}', title='Ejercicio 4')


def task5():
    r = abs(20 - (3 / 4) * (4 / 3) + 8)
    return d.msgbox(f'Implementar\nr = |20 − 3/5 ∗ 4/3 + 8|\n\nResult: {"{:.2f}".format(r)}', title="Ejercicio 5")


def task6():
    return make_form({
        "Valor de X": "",
    },
        title="Ejercicio 6",
        description="Implementar\nr = cos(2x+5)")


def task7():
    return make_form({
        "Valor de N": "",
        "Valor de X": "",
    },
        title="Ejercicio 6",
        description="Implementar\nr = cos(2x+5)")


def task8():
    r = math.log(15, 9)
    return d.msgbox(f'Implementar\nr = log9(15)\n\nResult: {"{:.2f}".format(r)}', title="Ejercicio 8")


def task9():
    r = math.log(7)
    return d.msgbox(f'Implementar\nr = log(7)\n\nResult: {"{:.2f}".format(r)}', title="Ejercicio 9")


def task10():
    code, data = make_form({
        'b': "",
        'c': "",
    }, title="Ejercicio 10",
        description="Implementar -b(+-)√(b**2 - 4ac) / 2a\ndonde:\n a = 𝜋\n b & c no se conocen")
    if code == d.OK:
        try:
            a, b, c = math.pi, float(data[0]), float(data[1])
            x = (b ** 2 - (4 * a * c)) ** 0.5
            r1 = x - b
            r2 = -1 * (x + b)
            return d.msgbox(f'Respuesta 1: {"{:.2f}".format(r1)}\nRespuesta 2: {"{:.2f}".format(r2)}',
                            title="Ejercicio 10")
        except ValueError:
            return d.msgbox(f'Por favor ingresa solo numeros', width=40, height=10)


def task11():
    r = pow(math.e, 0.6895528)
    return d.msgbox(f'Implementar\nr = e ** 0.6895528\n\nResult: {"{:.2f}".format(r)}', title="Ejercicio 11")


def task12(a=math.pi, b=-170):
    r = math.sqrt(a ** 2 + b ** 2)
    return d.msgbox(f'Implementar r = √(𝑎2 +𝑏2)\ndonde\n a = 𝜋\n b = -170\n\nResult: {"{:.2f}".format(r)}',
                    title="Ejercicio 12")


def task14():
    countries = {
        'Nicaragua': 20,
        'El Salvador': 25,
        'Honduras': 30,
        'Costa Rica': 35,
        'Guatemala': 30,
        'Panamá': 40,
        'Salir': 0,
    }
    code, tag = d.menu("Selecciona un pais",
                       choices=((key, key) for key in countries.keys()),
                       height=16)
    if tag != 'Salir':
        code, data = make_form({
            'Salario por hora': "",
            'Horas trabajadas': "",
        }, title="Seccion 2 - Ejercicio 8",
            description="Ingresa el salario por hora y las horas trabajadas")
        try:
            if code == d.OK:
                salary = float(data[0]) * float(data[1])
                r = salary - ((salary * countries[tag]) / 100)
                return d.msgbox(f'Salario neto a recibir: {"{:.2f}".format(r)}', width=40, height=10)
        except ValueError:
            return d.msgbox(f'Por favor ingresa solo numeros', width=40, height=10)


@click.command()
def main():
    code, tag = d.menu("Curso Python - Tarea 1",
                       choices=[("1", "Seccion I - Ejecicio 1"),
                                ("2", "Seccion I - Ejecicio 2"),
                                ("3", "Seccion I - Ejecicio 3"),
                                ("4", "Seccion I - Ejecicio 4"),
                                ("5", "Seccion I - Ejecicio 5"),
                                ("6", "Seccion I - Ejecicio 6"),
                                ("7", "Seccion I - Ejecicio 7"),
                                ("8", "Seccion I - Ejecicio 8"),
                                ("9", "Seccion I - Ejecicio 9"),
                                ("10", "Seccion I - Ejecicio 10"),
                                ("11", "Seccion I - Ejecicio 11"),
                                ("12", "Seccion I - Ejecicio 12"),
                                ("13", "Seccion II - Parte 1"),
                                ("14", "Seccion II - Parte 2"),
                                ],
                       height=16)

    if code == d.ESC:
        return terminate()
    else:
        if tag == '1':
            code, data = task1()
            if code == d.OK:
                now = datetime.now()
                d.msgbox(f'Bienvenido {data[0]} {data[1]} \n{now.strftime("%d/%m/%Y %H:%M:%S")}', width=40, height=10)

        elif tag == '2':
            code, data = task2()
            if code == d.OK:
                try:
                    result = (float(data[0]) + float(data[1]) + float(data[2])) - float(data[3]) + float(data[4]) ** 3
                    d.msgbox(f'La respuesta al problema es:[{result}]', width=40, height=10)
                except ValueError:
                    d.msgbox(f'Por favor ingresa solo numeros', width=40, height=10)

        elif tag == '3':
            task3()

        elif tag == '4':
            task4()

        elif tag == '5':
            task5()

        elif tag == '6':
            code, data = task6()
            if code == d.OK:
                try:
                    r = math.cos((2 * float(data[0])) + 5)
                    d.msgbox(f'Implementar\nr = cos(2x+5)\ncon x={data[0]}\n\nResult: {"{:.2f}".format(r)}',
                             title='Ejercicio 6')
                except ValueError:
                    d.msgbox(f'Por favor ingresa solo numeros', width=40, height=10)

        elif tag == '7':
            code, data = task7()
            if code == d.OK:
                try:
                    n = float(data[0])
                    x = float(data[1])
                    r = 1 + ((n * x) / math.factorial(1)) + (((n * (n - 1)) * x ** 2) / math.factorial(4))
                    d.msgbox(f'Implementar\n'
                             f'r = 1 + ((n * x) / 1!) + (((n * (n - 1)) * x^2) / 4!)\n'
                             f'con n={n}\n'
                             f'con x={x}\n\n'
                             f'Result: {"{:.2f}".format(r)}',
                             title='Ejercicio 7',
                             width=60)
                except ValueError:
                    d.msgbox(f'Por favor ingresa solo numeros', width=40, height=10)

        elif tag == '8':
            task8()

        elif tag == '9':
            task9()

        elif tag == '10':
            task10()

        elif tag == '11':
            task11()

        elif tag == '12':
            task12()

        elif tag == '13':
            webbrowser.open("https://colab.research.google.com/drive/1Bv3ZlnaORy5dWI5r8jEDrGznqap5Lfhv?usp=sharing")

        elif tag == '14':
            task14()

        elif tag == '0':
            return terminate()

    main()


if __name__ == "__main__":
    main()
