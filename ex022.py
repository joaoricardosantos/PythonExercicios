
nome = input('Digite seu nome completo: ').strip()
print(nome.upper())
print(nome.lower())
divido = nome.split()
print(len(nome) - nome.count(' '))
print(f'Seu primeiro nome é {divido[0]}')
print(f'Seu primeiro nome é {divido[0]} e tem {len(divido[0])} letras')
