import datetime
pessoa = dict()
pessoa['Nome'] = input('Nome: ').capitalize()
pessoa['Idade'] = int(input('Ano de nascimento: '))
pessoa['Ctps'] = int(input('Carteira de trabalho: '))
pessoa['Idade'] = datetime.date.today().year - pessoa['Idade']
if pessoa['Ctps'] != 0:
    pessoa['Contratacao '] = int(input('Ano de contratação: '))
    pessoa['Salario'] = float(input('Salário: R$'))
print('=-'*30)
for c, v in pessoa.items():
    print(f'{c} tem o valor {v}')