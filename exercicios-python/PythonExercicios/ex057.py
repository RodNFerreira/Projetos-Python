sexo = str(input('Digite o seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Tente novamente! '))
    if sexo in 'M' and 'F':
        print(f'Sexo {sexo} registrado com sucesso!')
