print('='*20)
print('10 TERMOS DE UMA PA')
print('='*20)
primeiro = int(input('Digite o primeiro valor da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print(f'{c}', end=' --> ')
print('ACABOU.')

