tot = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        tot += n
print(f'A soma de todos números pares foi de {tot}')