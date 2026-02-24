hVelho = 0
nVelho = ''
m20 = 0
totalIdade = 0


for c in range(0, 4):
    nome = input('Digite o seu nome: ')
    idade = int(input('Digite a sua idade: '))
    sexo = input('Digite o seu sexo (M/F): ').upper().strip()
    totalIdade += idade
    if sexo == 'M' and idade > hVelho:
        nVelho = nome
        hVelho = idade
    if sexo == 'F' and idade < 20:
        m20 += 1
mediaIdade = totalIdade / 4

print(f'A media da idade é de {mediaIdade}')
print(f'O nome do homem mais velho é {nVelho} e ele tem {hVelho} anos')
print(f'Quantidade de mulheres com menos de 20 anos {m20}')