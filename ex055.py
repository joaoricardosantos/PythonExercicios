maior = 0
menor = 1000
for c in range (0, 5):
    peso = float(input('Digite o seu peso: '))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso
print(f'O maior peso foi {maior} e o menor foi {menor}')
