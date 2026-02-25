numeros = ('Zero','Um', 'Dois', 'Trẽs', 'Quatro', 'Cinco', 'Seis',
           'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
           'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
           'Dezenove', 'Vinte')
escolha = int(input('Digite um número entre 0 e 20: '))
while True:
    if escolha > 20 or escolha < 0:
        escolha = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    else:
        break
print(f'Vocẽ digitou o número {numeros[escolha]}')