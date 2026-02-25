print(f'=-'*20)
print(f'LOJA PATRIKA')
print(f'=-'*20)
resp = 'S'
menor = soma = maisQueMil = 0
nomeMenor = ''
while resp  == 'S':
    nome = input('Nome do Produto: ')
    preco = float(input('Preço: R$'))
    if resp == 'S':
        menor = preco
        nomeMenor = nome
    if preco < menor:
        menor = preco
        nomeMenor = nome
    if preco >= 1000:
        maisQueMil += 1
    soma += preco
    resp = input('Quer continuar [S/N}: ').upper().strip()
print('-----------FIM DO PROGRAMA-----------')
print(f'Valor total da compra: R${soma:.2f}')
print(f'Produtos acima de que R$1000.00: {maisQueMil}')
print(f'O produto mais barato foi {nomeMenor}, custando R${menor:.2f}')
