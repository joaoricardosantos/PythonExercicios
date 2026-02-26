produtos = ('Notebook', 2559.00,
            'Monitor', 750.99,
            'Mouse', 59.99,
            'Teclado', 299.99,
            'Computador Gamer', 4599.99)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<30}', end=' ')
    else:
        print(f'R${produtos[item]:>9.2f}')
