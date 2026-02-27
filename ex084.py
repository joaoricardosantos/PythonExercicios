pessoas = list()
dados = list()
maiorPeso = menorPeso = 0
while True:
    dados.append(input('Nome: ').capitalize())
    dados.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maiorPeso = menorPeso = dados[1]
    else:
        if dados[1] > maiorPeso:
            maiorPeso = dados[1]
        if dados[1] < menorPeso:
            menorPeso = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    resp = input('Quer continuar? [S/N] ').upper().strip()[0]
    if resp == 'N':
        break
print('-=' *30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas. ')
print(f'O maior peso foi de {maiorPeso:.2f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maiorPeso:
        print(f'{p[0]}', end=' ')
print(f'\nO menor peso foi de {menorPeso:.2f}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menorPeso:
        print(f'{p[0]}', end=' ')