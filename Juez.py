def root(a, mov):
    if len(a) == 0:
        return a
    elif a[0] == ' ':
        return a[0] + root(a[1:], mov)
    else:
        aux = ord(a[0].lower()) + mov
        while aux > 122:
            aux -= 26
        return chr(aux) + root(a[1:], mov)


num = int(input().strip())
for i in range(num):
    rot = int(input().strip())
    frase = input().strip()
    print(root(frase, rot))
