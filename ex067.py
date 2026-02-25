cont = 0
while True:
    print('-'*30)
    tabuada = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    cont = 0
    if tabuada < 0:
        break
    while cont <= 10:
        print(f'{tabuada} x {cont} = {tabuada * cont}')
        cont += 1
print('PROGRAMA ENCERRADO. Volte sempre!')
