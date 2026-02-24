s = t = c = 0
while c != 999:
    c = int(input('Digite um valor (999 para sair): '))
    s += c
    t += 1
print(f'A quantidade de números digitados foi {t-1}')
print(f'A soma dos números totais(desconsiderando o flag) foi {s-c}')