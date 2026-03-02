jogador = dict()
jogador['Nome'] = input('Nome do Jogador: ').capitalize()
jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))
jogador['Gols'] = 0
for c in range(jogador['Partidas']):
    jogador['Gols'] = int(input(f'Quantos gols na partida {c}? '))
print(jogador)