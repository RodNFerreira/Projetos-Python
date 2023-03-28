real = float(input('Quanto dinheiro você quer converter? R$: '))
dolar = real / 5.33
euro = real / 5.42
print(f'R${real:.2f} valem US${dolar:.2f} e €{euro:.2f}')
