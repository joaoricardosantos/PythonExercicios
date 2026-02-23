n1 = int(input('Digite o 1o número: '))
n2 = int(input('Digite o 2o número: '))
n3 = int(input('Digite o 30 número: '))
if n1 > n2 and n1 > n3:
    print(f'O número 1o é o maior!')
elif n2 > n1 and n2 > n3:
    print(f'O número 2o é o maior!')
else:
    print(f'O número 3o é o maior!')
print('FIM DO PROGRAMA')