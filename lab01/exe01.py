''' Funciones para hallar el números mayor, el números menor y el números intermedio de una secuencia de 3 números '''

def maximum(a,b,c):
    vec = [a,b,c]
    aux = 0
    for num in vec:
        if num>aux:
            aux = num
    return aux

def minimum(a,b,c):
    vec = [a,b,c]
    aux = abs(a) + abs(b) + abs(c)
    for num in vec:
        if num<aux:
            aux = num
    return aux

def middle(a,b,c):
    top=maximum(a,b,c)
    bot=minimum(a,b,c)

    if a!=top and a!=bot:
        return a
    elif b!=top and b!=bot:
        return b
    elif c!=top and c!=bot:
        return c
    else:
        return "No hay intermedio"