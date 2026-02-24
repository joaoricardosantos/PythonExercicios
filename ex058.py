import random
from time import sleep
resp = 'S'
palp = 0
print('=-' * 20)
print('VOU PENSAR EM UM NÚMERO DE 0 A 10')
print('TENTE ADVINHAR O MESMO NÚMERO QUE EU')
print('=-' * 20)
while resp == 'S':
    comp = random.randint(0, 10)
    print('PENSANDO.')
    sleep(1)
    print('PENSANDO..')
    sleep(1)
    print('PENSANDO...')
    sleep(1)
    print('PENSEI!')
    jogador = int(input('QUAL FOI O NÚMERO QUE EU PENSEI? '))
    if jogador == comp:
        print('PARABÉNS VOCÊ VENCEU')
    else:
        print(f'GANHEI DE NOVO HAHAHA! O NÚMERO QUE EU PENSEI FOI {comp}')
    print('=-'*20)
    resp = input('QUER CONTINUAR (S/N)? ').upper().strip()
    print('=-' * 20)
    palp += 1
print('FIM')
print('=-'*20)
if palp == 1:
    print('UAU PARABÉNS VOCÊ GANHOU DE PRIMEIRA')
else:
    print(f'LEVOU {palp} PALPITES PARA ACERTAR')