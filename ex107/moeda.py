def metade(valor=0):
    valor = valor / 2
    return  valor

def dobro(valor=0):
    valor = valor * 2
    return valor

def aumento(valor=0, por = 0):
    valor = (valor * por / 100) + valor
    return valor

def reduzir(valor=0, por = 0):
    valor = valor - (valor * por / 100)
    return valor
