
def top(a,b,c):
    vec = [a,b,c]
    aux = 0
    for num in vec:
        if num>aux:
            aux = num
    return aux

def bot(a,b,c):
    vec = [a,b,c]
    aux = abs(a) + abs(b) + abs(c)
    for num in vec:
        if num<aux:
            aux = num
    return aux

def mid(a,b,c):
    up=top(a,b,c)
    down=bot(a,b,c)

    if a!=up and a!=down:
        return a
    elif b!=up and b!=down:
        return b
    elif c!=up and c!=down:
        return c
    else:
        return "No hay intermedio"