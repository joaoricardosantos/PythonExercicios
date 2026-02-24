from math import  factorial
from time import  sleep

n = int(input('Digite um número para calcular o seu fatorial: '))
f = factorial(n)
c = n
print(f'Calculuando {n}!.')
sleep(1)
print(f'Calculuando {n}!..')
sleep(1)
print(f'Calculuando {n}!...')
sleep(1)
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print(f)