sal = float(input('Digite o seu salário: R$'))
if sal > 1.250:
    novoSal = (sal * 10) / 100 + sal
else:
    novoSal = (sal * 15) / 100 + sal
print(f'O seu salário era de R${sal} e com o reajuste ficou R${novoSal}')