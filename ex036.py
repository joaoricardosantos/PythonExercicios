valor = float(input('Digite o valor da casa: R$'))
sal = float(input('Qual é o seu salário? R$'))
anos = int(input('Em quantos anos você irá pagar? '))
parcela = valor / (anos / 12)
if parcela > (sal * 30)/ 100:
    print('Emprestimo negado!')
else:
    print(print('Emprestimo aprovado!'))