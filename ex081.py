resp = ' '
valor = list()
cont = 0
while resp not in 'N':
    valor.append(int(input('Digite um valor: ')))
    cont += 1
    resp = input('Quer continuar? [S/N] ').upper().strip()[0]
    while resp not in 'SN':
        resp = input('Respota inválida, tente novamente. Quer continuar? [S/N] ').upper().strip()
valor.sort(reverse=True)
print('=-='*20)
print(f'Você digitou {cont} elementos.')
print(f'Os valores em ordem decresecente são {valor}')
if 5 in valor:
    print(f'O valor 5 faz parte da lista')
else:
    print(f'O valor 5 não faz parte da lista')