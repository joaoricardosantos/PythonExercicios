import moeda

p = float(input('Digite o valor: R$'))
print(f'A metade de {moeda.moeda(p)} é igual a {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é igual a {moeda.dobro(p, True)}')
print(f'Aumentando 10%, temos {moeda.aumento(p, 10, True)}')
print(f'Reduzindo 13%, temos {moeda.reduzir(p, 13, True)}')