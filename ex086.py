matiz = [[0,0,0], [0,0,0], [0,0,0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matiz[linha] [coluna] = int(input(f'Digite um valor para posição [{linha}, {coluna}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matiz[l] [c]:^5}]', end='')
    print()