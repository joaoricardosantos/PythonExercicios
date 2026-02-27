resp = ' '
valor = list()
while resp not in 'N':
    n = int(input('Digite um valor: '))
    if n not in valor:
        valor.append(n)
    else:
        print('Valor duplicado! Não vou adicionar')
    resp = input('Quer continuar? [S/N] ').upper().strip()[0]
    while resp not in 'SN':
        resp = input('Respota inválida, tente novamente. Quer continuar? [S/N] ').upper().strip()
valor.sort()
print(valor)