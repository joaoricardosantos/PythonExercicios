def metade(valor, format=False):
    valor = valor / 2
    return  valor if format is False else moeda(valor)

def dobro(valor, format=False):
    valor = valor * 2
    return valor if format is False else moeda(valor)

def aumento(valor, por, format=False):
    valor = (valor * por / 100) + valor
    return valor if format is False else moeda(valor)

def reduzir(valor, por, format=False):
    valor = valor - (valor * por / 100)
    return valor if format is False else moeda(valor)

def moeda(valor=0, moeda ='R$', format=False):
    return f'{moeda}{valor:.2f}'.replace('.', ',')