from PythonExercicios.ex107 import metade, dobro, aumento, reduzir

p = float(input('Digite o valor: R$'))
print(f'A metade de R${p} é igual a R${metade(p)}')
print(f'O dobro de R${p} é igual a R${dobro(p)}')
print(f'Aumentando 10%, temos R${aumento(p, 10)}')
print(f'Reduzindo 13%, temos R${reduzir(p, 13)}')