aluno = dict()
aluno['Nome'] = input('Nome: ').capitalize()
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))
aluno['Situação'] = ''
if aluno['Media'] > 6:
    aluno['Situação'] = 'APROVADO'
elif aluno['Media'] == 6:
    aluno['Situação'] = 'RECUPERAÇÂO'
else:
    aluno['Situação'] = 'REPROVADO'

print(f'O nome é igual a {aluno["Nome"]}')
print(f'A média é igual a {aluno["Media"]}')
print(f'A situação é igual a {aluno["Situação"]}')
