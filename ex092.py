import datetime
pessoa = dict()
pessoa['Nome'] = input('Nome: ').capitalize()
pessoa['Idade'] = int(input('Ano de nascimento: '))
pessoa['Ctps'] = int(input('Carteira de trabalho (0 não tem): '))
pessoa['Idade'] = datetime.date.today().year - pessoa['Idade']
if pessoa['Ctps'] != 0:
    pessoa['Contratacao '] = int(input('Ano de contratação: '))
    pessoa['Salario'] = float(input('Salário: R$'))
    pessoa['Aposentadoria'] = pessoa['Idade'] + ((pessoa['Contratacao '] + 35) - datetime.date.today().year)
print('=-'*30)
for c, v in pessoa.items():
    print(f'{c} tem o valor {v}')