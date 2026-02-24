idade = int(input('Digite a sua idade: '))
if idade < 18:
    print('Vocẽ ainda vai se alistar no serviço militar.')
elif idade == 18:
    print('É a hora de você se alistar!')
else:
    print('Já passou do tempo do seu alistamento')