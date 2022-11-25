print('Máxumo común divisor de 3 números')
num1 = int(input('Primer número:'))
num2 = int(input('Segundo número:'))
num3 = int(input('Tercer número:'))
MCD = 1
for i in range(1, num1 + 1):
    if num1 % i == 0 and num2 % i == 0 and num3 % i == 0:
        MCD = i
print('El máximo común divisor de', num1, ',', num2, 'y', num3, "es el", MCD)
