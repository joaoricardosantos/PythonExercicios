from random import randint
from time import sleep

jogadores = {
    'Jogador 1': randint(1, 6),
    'Jogador 2': randint(1, 6),
    'Jogador 3': randint(1, 6),
    'Jogador 4': randint(1, 6)
}
print('Valores sorteados:')
for k, v in jogadores.items():
    sleep(1)
    print(f'O {k} tirou: {v}')