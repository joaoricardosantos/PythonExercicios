import random

print('=-'*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*20)
v = 0
d = 0
s = 0
while d < 1:
    computador = random.randint(0, 10)
    jogador = int(input('VALOR: '))
    pi = str(input('PAR OU ÍMPAR? [P/I]: ')).upper().strip()[0]
    print('--'*20)
    s = jogador + computador
    if s % 2 == 0:
        if pi == 'P':
            print(f'Você jogou {jogador} e o computador jogou {computador}. TOTAL {s} DEU PAR')
            print('--' * 20)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('--' * 20)
            v += 1
        else:
            print(f'Você jogou {jogador} e o computador jogou {computador}. TOTAL {s} DEU PAR')
            print('Vocẽ PERDEU!')
            break
    if s % 2 == 1:
        if pi == 'I':
            print(f'Você jogou {jogador} e o computador jogou {computador}. TOTAL {s} DEU ÍMPAR')
            print('--' * 20)
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            print('--' * 20)
            v += 1
        else:
            print(f'Você jogou {jogador} e o computador jogou {computador}. TOTAL {s} DEU ÍMPAR')
            print('Vocẽ PERDEU!')
            break

print(f'FIM DE JOGO! Você venceu {v} vezes.')