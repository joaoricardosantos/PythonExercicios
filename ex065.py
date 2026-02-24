resp = ''
tot = maior = menor = media = 0

while not resp == 'N':
    n = int(input('Digite um número: '))
    media += 1
    tot += n
    if resp == '':
        menor = n
        maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = input('Deseja continuar (S/N): ').upper().strip()
print(f'A média entre todos os números digitados foi {tot / media}')
print(f'O maior número digitado foi {maior}')
print(f'O menor número digitado foi {menor}')