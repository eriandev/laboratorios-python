''' Operaciones básicas de suma, resta, multiplicación, división y potenciación para 2 números '''

def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    if b==0:
        return "No está definida la división entre 0" 
    else:
        return a/b

def power(a,b):
    return a**b