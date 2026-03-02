from random import randint
from time import sleep
from operator import itemgetter
jogadores = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
}
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print('Valores sorteados:')
for k, v in jogadores.items():
    sleep(1)
    print(f'O {k} tirou: {v}')
print('-' * 30)
print('     RANKING')
print('-' * 30)
for e, v in enumerate(rank):
    print(f'{e + 1} lugar: {v[0]} com {v[1]}')
    sleep(1)