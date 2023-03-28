casa = float(input('Qual é o valor da casa? R$'))
salario = float(input('Qual é o salário do comprador? R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'Para comprar uma casa de R${casa:.2f} em {anos} anos, a prestação será de R${prestacao:.2f}.')
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO!')
else:
    print('Empréstimo NEGADO!')
