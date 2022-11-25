print('El rey está o no en jaque')
corx_d = int(input('Coordenada x de la dama (Del 1 al 8):'))
cory_d = int(input('Coordenada y de la dama (Del 1 al 8):'))
corx_r = int(input('Coordenada x del rey (Del 1 al 8):'))
cory_r = int(input('Coordenada y del rey (Del 1 al 8):'))
if corx_d == corx_r or cory_d == cory_r or abs(corx_d - corx_r) == abs(cory_d - cory_r):
    print('Jaque')
else:
    print('No está en jaque')
