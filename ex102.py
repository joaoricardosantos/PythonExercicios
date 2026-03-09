def fatorial(n, show = False):
    """
    -> Calcula o fatorial de um número.
    :Parametro n: O número a ser calculado
    :Parametro show: (opcional) Mostrar ou não a conta.
    :return: O valor do fatorial de n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f

num = int(input('Digite um número: '))
mostrar = input('Deseja mostrar? [S/N] ').upper().strip()[0]
if mostrar in 'S':
    mostrar = True
else:
    mostrar = False
print(fatorial(num, mostrar))
help(fatorial)