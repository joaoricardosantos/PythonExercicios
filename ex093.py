jogador = dict()
partidas = list()
jogador['Nome'] = input('Nome do Jogador: ').capitalize()
jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
for c in range(jogador['Partidas']):
    partidas.append(int(input(f'Quantos gols na partida {c + 1}? ')))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for c, v in jogador.items():
    print(f'O campo {c} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]} partidas.')
for i, v in enumerate(jogador['Gols']):
    print(f'        => Na partida {i + 1}, fez {v} gols.')
print(f'Foi um total de {jogador["Total"]} gols')