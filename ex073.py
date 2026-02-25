brasileirao = ('Palmeiras', 'São Paulo', 'Fluminense', 'Bahia', 'Corinthians',
               'Athletico-PR', 'Bragantino', 'Chapecoense', 'Mirassol', 'Coritiba',
               'Flamengo', 'Botafogo', 'Grêmio', 'Vitória', 'Atlético Mineiro',
               'Remo-PA', 'Vasco da Gama', 'Santos', 'Internacional', 'Cruzeiro')
print('=-'*20)
print(f'Os 5 primeiros colocados {brasileirao[0:5]}')
print('=-'*20)
print(f'Os 4 últimos colocados {brasileirao[-4:]}')
print('=-'*20)
print(f'Times em ordem alfabétiica: {sorted(brasileirao)}')
print('=-'*20)
print('A Chapeconese está na ', brasileirao.index('Chapecoense')+1,'ª posição')