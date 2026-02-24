n = int(input('Digite um número: '))
p = 0
for c in range(2, n):
    if n % c == 0:
        p += 1
if p > 1:
    print(f'O número {n} não é primo.')
else:
    print(f'O número {n} é primo')