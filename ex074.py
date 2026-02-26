from random import randint

numeros = randint(0, 10), randint(0, 10),randint(0, 10), randint(0, 10),randint(0, 10)
print('Os valores sorteados foram:', end=' ')
for n in numeros:
    print(n, end=' ')
print('FIM')
print(f'O maior número foi: {max(numeros)} e o menor foi {min(numeros)}')