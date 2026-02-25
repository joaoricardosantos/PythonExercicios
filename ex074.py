from random import randint

numeros = randint(0, 10), randint(0, 10),randint(0, 10), randint(0, 10),randint(0, 10)
maior = cont = menor = 0
for cont in range(0, len(numeros)):
    if cont == 0:
        if numeros[cont] > maior:
            maior = numeros[cont]
        if numeros[cont] < menor:
            menor = numeros[cont]
    print(numeros[cont], end=' ')
    cont += 1
print('FIM')
print(f'O maior número foi: {maior} e o menor foi {menor}')