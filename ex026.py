frase = input('Digite a sua frase: ').strip().lower()
print('A letra a apareceu na sua frase', frase.count('a'), 'vezes')
print(f'A primeira letra A apareceu na posição: ', frase.find('a')+1)
print('A última letra A apareceu na posição: ', frase.rfind('a') +1)