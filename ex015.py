dias = int(input('Qual a quantidade de dias que o carro foi alugado? '))
totDias = 60 * dias
km = float(input('Quantos Kms foi percorrido? '))
totKM = km * 0.15
totalPagar = totKM + totDias
print(f'O valor a pagar será de {totalPagar:.2f}R$')