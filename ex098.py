from time import sleep


def contador():
    print('-=' * 20)
    print('Contagem de 1 até 10 de 1 em 1!')
    for cont in range(1, 11):
        sleep(0.3)
        print(cont ,end=' ')
    print('FIM')
    print('-=' * 20)
    print('Contagem de 10 até 0 de 2 em 2!')
    for cont in range(10, -1, -2):
        sleep(0.3)
        print(f'{cont} ', end=' ')
    print('FIM')
    print('-=' * 20)
    print('Agora é a sua vez de personalizar a contagem!')
    i = int(input('Inicio: '))
    f = int(input('Fim: '))
    p = int(input('Passo: '))
    print('-=' * 20)
    if p == 0:
        p = 1
    if i > f:
        p = -abs(p)
        f -= 1
        print(f'Contagem de {i} até {f+1} de {p} em {p}')
    else:
        f += 1
        print(f'Contagem de {i} até {f-1} de {p-1} em {p}')
    for cont in range(i, f, p):
        sleep(0.3)
        print(cont, end=' ')

contador()