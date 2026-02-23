km = int(input('Quantos Km/h estava o seu carro? '))
multa = km
if km > 80:
    print(f'Você foi multado!')
    multa = (km - 80) * 7
    print(f'Você terá que pagar uma multa de R${multa:.2f}')
print('Bom dia, Dirija com segurança!')