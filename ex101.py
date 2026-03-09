def voto(ano):
    from datetime import date
    anoAtual = date.today().year
    idade = anoAtual - ano
    if idade < 16:
        return f'Com {idade} anos, o você ainda não vota.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos, o seu voto é opcional.'
    else:
        return f'Com {idade} anos, o seu voto é obrigatorio.'


nascimento = int(input('Em que ano você nasceu: '))
print(voto(nascimento))
