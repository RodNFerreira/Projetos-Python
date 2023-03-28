from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual-nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Sua classificação é MIRIM.')
elif 9 < idade <= 14:
    print('Sua classificação é INFANTIL.')
elif 14 < idade <= 19:
    print('Sua classificação é JUNIOR.')
elif 19 < idade <= 25:
    print('Sua classificação é SENIOR.')
else:
    print('Sua classificação é MASTER.')
