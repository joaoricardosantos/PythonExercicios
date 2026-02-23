km = float(input('Digite a distância da viagem: '))
if km <= 200:
    preco = km * 0.50
else:
    preco = km * 0.45
print(f'O valor a pagar no total será de {preco:.2f}R$')