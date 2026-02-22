from math import sqrt

compOposto = float(input('Digite o comprimento do cateto oposto: '))
compAdjacente = float(input('Digite o comprimento do cateto adjacente: '))
hipo = sqrt(compOposto ** 2 + compAdjacente ** 2)
print(f'A hipotenusa é igual a {hipo}')