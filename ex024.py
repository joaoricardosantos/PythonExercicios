cidade = input('Digite o nome da sua cidade: ').strip( )
cidade = cidade.lower()
santos = cidade.split()
print('santos' in santos[0])