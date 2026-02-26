resp = ' '
valor = list()
while resp not in 'N':
    valor.append(int(input('Digite um valor: ')))
    resp = input('Quer continuar? [S/N] ').upper().strip()[0]
    while resp not in 'SN':
        resp = input('Respota inválida, tente novamente. Quer continuar? [S/N] ').upper().strip()
valor.sort()
print(valor)