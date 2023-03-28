dias = float(input('Quantos dias o carro foi alugado? '))
km = float(input('Quantos km foram rodados? '))
pago = (dias * 60) + (km * 0.15)
print(f'O aluguel do carro fica em R${pago:.2f}')

