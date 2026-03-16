from .moeda import metade, dobro, aumento, reduzir

p = float(input('Digite o valor: '))
print(f'A metade de R${p} é igual a {metade(p)}')
print(f'O dobro de R${p} é igual a {dobro(p)}')
print(f'Aumentando 10%, temos {aumento(p, 10)}')
print(f'Reduzindo 13%, temos {reduzir(p, 13)}')