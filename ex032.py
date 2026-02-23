from datetime import date
ano = int(input('Digite em que ano estamos (Coloque 0 para analisar o ano atual): '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 !=0 or ano % 400 == 0:
    print(f'{ano} É um ano BISSEXTO')
else:
    print(f'{ano} Não é um ano BISSEXTO')