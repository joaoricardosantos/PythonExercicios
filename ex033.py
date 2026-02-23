n1 = int(input('Digite o 1o número: '))
n2 = int(input('Digite o 2o número: '))
n3 = int(input('Digite o 3o número: '))
menor = n1
maior = n1
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
else:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n1:
    menor = n2
else:
    menor = n3
print(f'O maior número foi {maior} e o menor foi {menor}')
print('FIM DO PROGRAMA')