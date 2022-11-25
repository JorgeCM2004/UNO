print('Números ondulados')
num = int(input('Introduzca un número para saber si es ondulado o no:'))
cifras = 0
while num // 10 ** cifras != 0:
    cifras += 1
if cifras < 3:
    print('No es un número ondulado')
for i in range(cifras, 1, -2):
    num = num - (num // 10 ** (cifras - 2)) * 10 ** (cifras - 2)
    cifras -= 2
if num == 0 or num - (num // 10 ** (cifras - 1)) * 10 ** (cifras - 1) == 0:
    print('Es un número ondulado')
else:
    print('No es un número ondulado')
