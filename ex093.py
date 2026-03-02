jogador = dict()
jogador['Nome'] = input('Nome do Jogador: ').capitalize()
jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
jogador['Gols'] = list()
for c in range(jogador['Partidas']):
    jogador['Gols'] = int(input(f'Quantos gols na {c + 1}o. partida? '))
print(jogador)