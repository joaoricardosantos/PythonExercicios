from random import randint
from time import sleep

jogos = list()
lista = list()

print('-' * 40)
print('JOGO DA MEGA SENA')

print('-' * 40)
vezes = int(input('Quantos jogos você quer gerar? '))
tot = 1
while tot <= vezes:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-='*3, f'SORTEANDO {vezes} JOGOS ', '-='*3)
for i, l, in enumerate(jogos):
    sleep(1)
    print(f'Jogo {i+1}: {l}')
print('-='*5, 'BOA SORTE!', '-='*5)


