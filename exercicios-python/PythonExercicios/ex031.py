km = float(input('Qual é a distância da viagem? '))
if km > 200:
    print(f'O preço da viagem ser de R${km * 0.45:.2f}')
else:
    print(f'O preço da viagem vai ser de R${km * 0.50:.2f}.')
