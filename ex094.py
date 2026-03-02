galera = list()
pessoa = dict()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = input('Digite o nome: ').title()
    while True:
        pessoa['Sexo'] = input('Digite o sexo: [M/F] ').upper().strip()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Apenas M ou F')
    pessoa['Idade'] = int(input('Digite a idade: '))
    soma += pessoa['Idade']
    galera.append(pessoa.copy())
    while True:
        resposta = input('Deseja continuar? [S/N] ').upper().strip()[0]
        if resposta in 'SN':
            break
        print('ERRO! Apenas S ou N')
    if resposta == 'N':
        break
print('-=' * 30)
print(galera)
print(f'A) Ao todos temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'B) A media de idade é de {media:5.2f} anos')
print(f'C) As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]} ', end='')
print('\nD) Lista de pessoas que estão acima da média: ', end='')
for p in galera:
    if p['Idade'] >= media:
        print(f'{p["Nome"]} ', end='')
print('-=' * 30)
