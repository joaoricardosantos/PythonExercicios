tot = 0
for c in range(1, 500):
    if c % 2 == 1 and c % 3 == 0:
        tot += c
    print(c)
print(f'A soma de todos os números impares que são multiplos de 3 é {tot}')

