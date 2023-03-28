peso = float(input('Qual é seu peso? (Kg)'))
altura = float(input('Qual é a sua altura? (m)'))
imc = peso / (altura ** 2)
print(f'O seu IMC é de {imc:.1f}.')
if imc < 18.5:
    print('Você está na faixa ABAIXO DO PESO.')
elif 18.5 <= imc < 25:
    print('Você está na faixa de peso IDEAL.')
elif 25 <= imc < 30:
    print('Você está na faixa de SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está na faixa de OBESIDADE.')
else:
    print('Você está na faixa de OBESIDADE MÓRBIDA.')

