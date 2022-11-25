def numero_nuggets(num):
    i = 1
    for a in range(num // 6 + 1):
        for b in range(num // 9 + 1):
            for c in range(num // 20 + 1):
                if a * 6 + b * 9 + c * 20 == num:
                    if True:
                        print('Solución: ', i)
                        print('Cajas de 6 nuggets: ', a)
                        print('Cajas de 9 nuggets: ', b)
                        print('Cajas de 20 nuggets: ', c)
                        print()
                        i += 1
    return False


x = int(input('Numero de nuggets que quieres comprar: '))
numero_nuggets(x)
