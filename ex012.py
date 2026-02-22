preco = float(input('Digite o valor do produto desejado: '))
desc = (preco * 5) / 100
precoComDesconto = preco - desc
print(f'O valor com 5% de desconto desse produto fica: {precoComDesconto:.2f}R$')
