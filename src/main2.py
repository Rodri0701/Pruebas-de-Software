def sum(x, y):
    return x + y

def sub(x, y):
    return x - y

def div(x, y):
    if y == 0:
        raise ValueError ("No se puede dividir entre 0")
    return x / y