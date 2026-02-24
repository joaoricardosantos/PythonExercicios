maior = 0
menor = 0
for c in range(0, 7):
    idade = int(input('Digite sua idade: '))
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'O total de pessoas que atingiram a maior idade foi de {maior}')
print(f'O total de pessoas menores de idade foi de {menor}')