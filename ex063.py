n1 = int(input('Digite um número: '))
n2 = n1 + (n1 - 1)
n3 = n1 + n2
termo = int(input('Quantos termos? '))
cont = 0
while not cont == termo:
    print(n1)
    n1 = n2
    n2 = n3
    print(n1 + n2)
    cont += 1