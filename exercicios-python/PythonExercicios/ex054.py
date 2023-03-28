from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pess in range(1, 8):
    nasc = int(input(f'Digite o ano de nascimento da {pess}° pessoa: '))
    idade = atual - nasc
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
print(f'Nesse grupo de pessoas, {totmaior} são MAIORES de idade e {totmenor} são MENORES de idade.')
