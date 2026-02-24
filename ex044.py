preco = float(input('Qual o preço do produto? R$'))
pagamento = int(input("""Qual a forma de pagamento?
[1] Á vista no dinheiro/cheque: 10% de desconto
[2] Á vista no cartão: 5% de desconto
[3] em até 2x no cartão: preço normmal
[4] 3x ou mais no cartão: 20% de juros
---------------------------------------
"""))
if pagamento == 1:
    preco = preco - (preco * 10) / 100
elif pagamento == 2:
    preco = preco - (preco * 5) / 100
elif pagamento == 3:
    preco = preco
elif pagamento == 4:
    preco = preco + (preco * 20) / 100
else:
    print(f'Forma de pagamento inválida.')
print(f'Com a forma de pagamento desejada, o valor R${preco:.2f}')