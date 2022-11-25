protagonista = input()
contadorB = 0
contadorN = 0
for i in range(8):
    piezas = str(input())
    for x in piezas:
        if x == 'p':
            contadorB += 1
        elif x == 'P':
            contadorN += 1
        if x == 'a':
            contadorB += 3
        elif x == 'A':
            contadorN += 3
        if x == 'c':
            contadorB += 3
        elif x == 'C':
            contadorN += 3
        if x == 'd':
            contadorB += 10
        elif x == 'D':
            contadorN += 10
        if x == 't':
            contadorB += 5
        elif x == 'T':
            contadorN += 5
if protagonista == 'Negras':
    print(contadorB - contadorN)
else:
    print(contadorN - contadorB)
