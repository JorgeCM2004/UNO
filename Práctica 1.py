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
    c = 4
    print('La longitud del lado del cuadrado es: ', c)
    print('El perímetro del cuadrado es: ', 4 * c)
    print('El área del cuadrado es: ', c ** 2)
    time.sleep(2)


def accion2():
    b = 4
    h = 6
    print('Base del triángulo: ', b)
    print('Altura del triángulo: ', h)
    print('El área del triángulo es: ', b * h / 2)
    time.sleep(2)


def accion3():
    b = 4
    h = 3
    print('Lado 1 del rectángulo: ', b)
    print('Lado 2 del rectángulo: ', h)
    print('El perímetro del rectángulo es: ', 2 * b + 2 * h)
    print('El área del rectángulo es: ', b * h)
    time.sleep(2)


def accion4():
    c = float(input('Lado del cuadrado:'))
    print('El perímetro del cuadrado es: ', 4 * c)
    print('El área del cuadrado es: ', c ** 2)
    time.sleep(2)


def accion5():
    b = float(input('Lado 1 del rectángulo: '))
    h = float(input('Lado 2 del rectángulo: '))
    print('El perímetro del rectángulo es: ', 2 * b + 2 * h)
    print('El área del rectángulo es: ', b * h)
    time.sleep(2)


def accion6():
    b = float(input('Base del triángulo: '))
    h = float(input('Altura del triángulo: '))
    print('El área del triángulo es: ', b * h / 2)
    time.sleep(2)


def accion7():
    a = float(input('Primer lado del triángulo: '))
    b = float(input('Segundo lado del triángulo: '))
    c = float(input('Tercer lado del triángulo: '))
    d = (a + b + c) / 2
    e = math.sqrt(d * (d - a) * (d - b) * (d - c))
    print('El perímetro del triángulo es: ', a + b + c)
    print('El área del triángulo es: ', e)
    time.sleep(2)


def accion8():
    a = float(input('Primer lado del triángulo: '))
    b = float(input('Segundo lado del triángulo: '))
    c = float(input('Ángulo del triángulo: '))
    e = 1 / 2 * a * b * math.sin(c * math.pi / 180)
    print('El área del triángulo es: ', e)
    time.sleep(2)


def accion9():
    a = float(input('Grados Fahrenheit: '))
    print('Grados Centígrados: ', 5 * (a - 32) / 9)
    time.sleep(2)


def accion10():
    x1 = float(input('Cordenada x del punto 1: '))
    y1 = float(input('Cordenada y del punto 1: '))
    x2 = float(input('Cordenada x del punto 2: '))
    y2 = float(input('Cordenada y del punto 2: '))
    print('La distancia entre los dos puntos es: ', math.sqrt((x2 - x1)**2 + (y2 - y1)**2))
    time.sleep(2)


def accion11():
    a = str(input('Nombre: '))
    x = 1
    while x <= 1000:
        print(a, end=' ')
        x = x + 1
    time.sleep(2)


def accion12():
    frase = str(input('Dame un frase: '))
    fseparada = frase.split(' ')

    # Leemos carácter a carácter, únicamente se transforman los carácteres del 0 al 9
    print('Primera solucion')
    for i in range(frase.__len__()):
        print(numero_a_letra(frase[i]), end='')
    print()

    # 2ª forma: se carga en un array las palabras y se recorre cada una
    print('Segunda solucion')
    for i in range(fseparada.__len__()):
        print(numero_a_letra(fseparada[i]), end=' ')
    time.sleep(2)


def accion13():
    a = float(input('Primer número: '))
    b = float(input('Segundo número: '))
    if a == b:
        print('Es True que ' + str(a) + ' y ' + str(b) + ' son iguales')
    else:
        print('Es False que ' + str(a) + ' y ' + str(b) + ' son iguales')
    time.sleep(2)


def accion14():
    ventas = float(input('Total de ventas el ultimo mes: '))
    salario = 1500
    salario_bruto = salario + 0.03 * ventas
    salario_neto = salario_bruto - salario_bruto * 0.18
    print('Salario bruto:', salario_bruto)
    print('Salario neto:', salario_neto)
    print('Descuentos por IRPF:', salario_bruto * 0.18)
    time.sleep(2)


def accion15():
    euros = float(input('Dame una cantidad de euros: '))
    interes = float(input('Dame una tasa de interés (en % pero sin incluirlo): '))
    anos = float(input('Dame un número de años: '))
    print('El dinero se convertirá en ' + str(euros * (1 + interes / 100) ** anos) + ' euros.')
    time.sleep(2)


def salir():
    print('Saliendo')


def numero_a_letra(x):
    if x == '0':
        return 'cero'
    elif x == '1':
        return 'un'
    elif x == '2':
        return 'dos'
    elif x == '3':
        return 'tres'
    elif x == '4':
        return 'cuatro'
    elif x == '5':
        return 'cinco'
    elif x == '6':
        return 'seis'
    elif x == '7':
        return 'siete'
    elif x == '8':
        return 'ocho'
    elif x == '9':
        return 'nueve'
    else:
        return x


if __name__ == '__main__':
    menu_principal()
