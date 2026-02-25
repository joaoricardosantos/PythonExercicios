print('=-'*20)
print('INICIO DO PROGRAMA')
print('=-'*20)
resp = 'S'
maiorIdade = 0
homens = 0
mulheresMenor20 = 0
while resp in 'S':
    print('--'*20)
    print('CADASTRE UMA PESSOA')
    print('=-' * 20)
    idade = int(input('IDADE: '))
    if idade > 18:
        maiorIdade += 1
    sexo = ''
    while not sexo == 'MF':
        sexo = str(input('SEXO: ')).upper().strip()
        if sexo in'MF':
            break
        else:
            continue
    if sexo == 'M':
        homens += 1
    elif sexo == 'F' and idade < 20:
        mulheresMenor20 += 1
    resp = input('QUER CONTINUAR [S/N]? ').upper().strip()
    if resp == 'N':
        break
    while not resp == 'S':
        resp = input('QUER CONTINUAR [S/N]? ').upper().strip()
        if resp in'S':
            break
        elif resp in 'N':
            break
print(f'Total de pessoas com mais de 18 anos: {maiorIdade}')
print(f'Total de homens cadastrados: {homens}')
print(f'Total de mulheres com menos de 20 anos cadastradas: {mulheresMenor20}')