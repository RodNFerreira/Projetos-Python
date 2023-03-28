larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = alt*larg
tinta = area / 2
print(f'Sua parede tem a dimensão de {larg}x{alt}, sendo assim, sua área é de {area}m².')
print(f'E, para pintar esta parede, será necessário {tinta:.0f} litros de tinta.')

