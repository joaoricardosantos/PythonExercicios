def metade(valor):
    valor = valor / 2
    return  valor

def dobro(valor):
    valor = valor * 2
    return valor

def aumento(valor, por):
    valor = (valor * por / 100) + valor
    return valor

def reduzir(valor, por):
    valor = valor - (valor * por / 100)
    return valor

def moeda(valor=0, moeda ='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')