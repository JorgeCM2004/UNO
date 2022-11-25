import time
import math


def mostrar_menu(opciones):
    print('Seleccione una opción:')
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := int(input('Opción: '))) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()


def menu_principal():
    opciones = {
        1: ('Práctica 1', accion1),
        2: ('Práctica 2', accion2),
        3: ('Práctica 3', accion3),
        4: ('Práctica 4', accion4),
        5: ('Práctica 5', accion5),
        6: ('Práctica 6', accion6),
        7: ('Práctica 7', accion7),
        8: ('Práctica 8', accion8),
        9: ('Práctica 9', accion9),
        10: ('Práctica 10', accion10),
        11: ('Práctica 11', accion11),
        12: ('Práctica 12', accion12),
        13: ('Práctica 13', accion13),
        14: ('Práctica 14', accion14),
        15: ('Práctica 15', accion15),
        16: ('Salir', salir)
    }
    generar_menu(opciones, 16)


def accion1():
    a = float(input('Número flotante: '))
    if a < 0:
        print('El número es negativo')
    time.sleep(2)


def accion2():
    a = float(input('Número flotante: '))
    if a >= 0:
        print('El número es positivo')
    time.sleep(2)


def accion3():
    a = int(input('Edad primera persona: '))
    b = int(input('Edad segunda persona: '))
    if a < b:
        print('La primera persona es más joven')
    elif b < a:
        print('La segunda persona es más joven')
    else:
        print('Ambas personas tienen la misma edad')
    time.sleep(2)


def accion4():
    caracter = str(input('Introduce un carácter: '))
    while caracter.__len__() != 1:
        caracter = str(input('Hay más de un carácter, por favor introduzca un solo caracter: '))
    if caracter == '(' or ')':
        print('Es un paréntesis')
    else:
        print('Este carácter no es un paréntesis')
    time.sleep(2)


def accion5():
    num = int(input('Escribe un numero entero: '))
    division = num / 2
    if float(division) == int(division):
        print(num, 'es par.')
    else:
        print(num, 'es impar.')
    time.sleep(2)


def accion6():
    num = int(input('Escribe un numero entero: '))
    doble = num / 2
    if float(doble) == int(doble):
        division = doble / 2
        if float(division) == int(division):
            print(num, 'es el doble de', int(doble), 'que es par.')
        else:
            print(num, 'es el doble de', int(doble), 'que es impar.')
    else:
        print('Este número no es el doble de ningón otro número.')
    time.sleep(2)


def accion7():
    num1 = int(input('Primer número: '))
    num2 = int(input('Segundo número: '))
    if num1 ** 2 == num2:
        print('El segundo es el cuadrado del primero.')
    elif num1 ** 2 > num2:
        print('El segundo es menor que el cuadrado del primero.')
    else:
        print('El segundo es mayor que el cuadrado del primero.')
    time.sleep(2)


def accion8():
    dinero = int(input('Dinero: '))
    cambio = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    i = 0
    while dinero > 0:
        if dinero // cambio[i] > 0:
            print('El número de billetes de ' + str(cambio[i]) + ' es ' + str(dinero // cambio[i]))
            dinero = dinero % cambio[i]
        i = i + 1
    time.sleep(2)


def accion9():
    print('Dame 5 numeros: ')
    num = float(input('Número 1: '))
    mayor = num - 1
    for i in range(4):
        num = float(input('Número ' + str(i + 2) + ': '))
        if num > mayor:
            mayor = num
    print('El número más grande es: ', mayor)
    time.sleep(2)


def accion10():
    x1 = float(input('Cordenada x del punto 1: '))
    y1 = float(input('Cordenada y del punto 1: '))
    x2 = float(input('Cordenada x del punto 2: '))
    y2 = float(input('Cordenada y del punto 2: '))
    print('La distancia entre los dos puntos es: ', math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
    time.sleep(2)


def accion11():
    a = str(input('Nombre: '))
    x = 1
    while x <= 1000:
        print(a, end=' ')
        x = x + 1


def accion12():
    print('Has elegido la opción 3')


def accion13():
    print('Has elegido la opción 3')


def accion14():
    print('Has elegido la opción 3')


def accion15():
    print('Has elegido la opción 3')


def salir():
    print('Saliendo')


if __name__ == '__main__':
    menu_principal()
