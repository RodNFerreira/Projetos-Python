salário = float(input('Qual o seu salário? '))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print(f'Quem ganhava R${salário:.2f}, vai passar a ganhar R${novo:.2f}')
