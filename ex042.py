r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('Pode formar um triângulo!')
    if r1 == r2 and r2 == r3:
        print('Equilátero: Todos os lados iguais!')
    elif r1 != r2 and r2 != r3:
        print('Escaleno: Todos os lados diferentes')
    else:
        print('Isósceles: Dois lados iguais')
else:
    print('Não pode formar um triângulo :(')
