import moeda

p = float(input('Digite o valor: R$'))
print(f'A metade de {moeda.moeda(p)} é igual a {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é igual a {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumento(p, 10))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.reduzir(p, 13))}')