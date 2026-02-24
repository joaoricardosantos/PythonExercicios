casa = float(input('Valor da casa: R$'))
sal = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de finaciamento? '))
prestacao = casa / (anos * 12)
minimo = sal * 30 / 100
print(f'Para pagar uma casa de R${casa:.2f} em {anos} anos', end='')
print(f'a prestação será de R${prestacao:.2f}')

if prestacao > minimo:
    print(f'EMPRESTIMO NEGADO')

else:
    print('EMPRESTIMO APROVADO')