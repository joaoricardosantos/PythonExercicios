valores = list()
maior = menor = 0
for  cont in range(0, 5):
    valores.append(int(input(f'Digite o valor para posição {cont}: ')))
    if cont == 0:
        menor = maior = valores[cont]

    else:
        if valores[cont] > maior:
            maior = valores[cont]
        if valores[cont] < menor:
            menor = valores[cont]
print('=-='*20)
print(f'Você digitou os valores {valores}')
print(f'Maior  valor digitado foi {maior} na posições: ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}...', end='')
print(f'\nO menor valor digitado foi {menor} na posições: ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')