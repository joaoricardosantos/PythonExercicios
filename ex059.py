opcao = 0
while opcao != 5:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    print('=-' * 20)
    print('O que deseja realizar com esses valores? ')
    print('[ 1 ] SOMAR')
    print('[ 2 ] MULTIPLICAR')
    print('[ 3 ] MAIOR')
    print('[ 4 ] NOVOS NÚMEROS')
    print('[ 5 ] SAIR')
    print('=-' * 20)
    opcao = int(input('OPÇÃO: '))
    if opcao == 1:
        print('=-' * 20)
        print(f'A soma entre {n1} e {n2} é igual a {n1 + n2}')
        print('=-'*20)
    elif opcao == 2:
        print('=-' * 20)
        print(f'A multiplicação entre {n1} e {n2} é igual a {n1 * n2}')
        print('=-' * 20)
    elif opcao == 3:
        if n1 > n2:
            print('=-' * 20)
            print(f'O valor {n1} é maior que o segundo valor')
            print('=-' * 20)
        else:
            print('=-' * 20)
            print(f'O valor {n2} é maior que o primeiro valor')
            print('=-' * 20)
    elif opcao == 4:
        continue
    else:
        print('Opção errada... tente novamente')
print('=-'*20)
print('FIM DO PROGRAMA')

