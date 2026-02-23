import random
n = random.randint(0, 5)
print('Vou pensar em um número entre 0 e 5...')
guess = int(input('Qual número eu pensei? '))
if guess == n:
    print(f'Parabens o número que eu pensei foi esse mesmo!')
else:
    print(f'HAHA ganhei, o número que eu pensei foi {n}')