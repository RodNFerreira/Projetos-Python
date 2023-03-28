from datetime import date

atual = date.today().year
nasc = int(input('Qual foi seu ano de nascimento? '))
idade = atual - nasc
print(f'Quem nasceu em {nasc} tem {idade} anos em {atual}.')
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    print(f'Você tem {idade} anos. Ainda faltam {18 - idade} anos para o alistamento.')
    print(f'Seu alistamento será em {nasc + 18}.')
elif idade > 18:
    print(f'Você já deveria ter se alistado a {idade - 18} anos.')
    print(f'Seu alistamento foi em {nasc + 18}')
