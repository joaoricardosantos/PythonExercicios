lista = list()
par = list()
impar = list()
while True:
    lista.append(int(input('Digite um número: ')))
    resp = input('Quer continuar? [S/N] ').upper().strip()[0]
    while resp not in 'SN':
        resp = input('Tente novamente. Quer continuar? [S/N] ').upper().strip()[0]
    if resp in 'N':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'A lista completa de números é {lista}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')