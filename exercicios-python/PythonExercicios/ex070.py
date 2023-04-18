tot = totmil = menor = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço: R$'))
    cont += 1
    tot += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format('FIM DO PROGRAMA!'))
print(f'O total da compra foi de R${tot:.2f}.')
print(f'Temos {totmil} produtos acima de R$1000,00.')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}.')


