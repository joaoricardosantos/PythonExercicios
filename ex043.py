peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura (em metros): '))
imc = peso / (altura * altura)
if imc < 18.5:
    print('Abaixo do peso.')
elif 18.5 <= imc <= 24.9:
    print('Peso normal')
elif 25 <= imc <=29.9:
    print('Sobrepeso')
elif 30 <= imc <=34.9:
    print('Obesidade Grau I')
elif 35 <= imc <= 39.9:
    print('Obesidade Grau II')
else:
    print('Obesidade Grau III')

print(f'{imc:.2f}')