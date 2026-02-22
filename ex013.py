sal = float(input('Digite o seu salário atual: '))
aumento = (sal * 15) / 100
novoSal = sal + aumento
print(f'O seu salário de R${sal:.2f} teve um aumento de 15%(R${aumento:.2f}) e seu novo salário agora é de R${novoSal:.2f}')