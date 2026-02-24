n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))

if n2 > n1:
    print(f'O número 2o é maior!')
elif n1 > n2:
    print(f'O valor 1o é maior')
else:
    print('Não existe valores maiores, os dois são iguais')