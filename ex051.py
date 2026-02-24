i = int(input('INICIO: '))
r = int(input('RAZAO: '))
decimo =  i + (10 - 1) * r
for c in range(i, decimo + r, r):
    print(' ',c, end=' -> ')
print('FIM')