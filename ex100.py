from random import  randint
from time import sleep

def sorteia(lista):
    print(f'Sorteando 5 valores da lista:', end=' ')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(n, end=' ')
        sleep(0.3)
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for num in lista:
        if num % 2 == 0:
            soma += num
    print(f'Somando os valores pares de {lista}, temos {soma}')




numeros = list()
sorteia(numeros)
somaPar(numeros)

