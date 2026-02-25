n = s = t = cont = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
    t += 1
print(f'A soma de todos os números é: {s}')
print(f'Total de números digitados: {t}')
