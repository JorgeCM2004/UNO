a = int(input('Primer número:'))
b = int(input('Segundo número:'))
while not a == b:
    if a > b:
        a = a - b
    else:
        b = b - a
print('El MCD es:', b)
