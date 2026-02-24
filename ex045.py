import  random

print('Bem vindo ao jogo de JOKENPÔ!')
print('=-'*20)
print('Escolha uma das opções para jogar contra o computador!')
print('[1] PEDRA')
print('[2] PAPEL')
print('[3] TESOURA')
print('=-'*20)
computador = random.randint(1, 3)
escolha = int(input('Escolha a sua jogada: '))
if escolha == computador:
    print('EMPATE!')
elif escolha == 2 and computador == 1:
    print(f'VOCÊ VENCEU... O COMPUTADOR JOGOU [{computador}] PEDRA')
elif escolha == 2 and computador == 3:
    print(f'VOCÊ PERDEU... O COMPUTADOR JOGOU [{computador}] TESOURA')
elif escolha == 1 and computador == 2:
    print(f'VOCÊ PERDEU... O COMPUTADOR JOGOU [{computador}] PAPEL')
elif escolha == 1 and computador == 3:
    print(f'VOCÊ VENCEU... O COMPUTADOR JOGOU [{computador}] TESOURA')
elif escolha == 3 and computador == 1:
    print(f'VOCÊ PERDEU... O COMPUTADOR JOGOU [{computador}] PEDRA')
elif escolha == 3 and computador == 2:
    print(f'VOCÊ VENCEU... O COMPUTADOR JOGOU [{computador}] PAPEL')
else:
    print('OPÇÃO INVÁLIDA')