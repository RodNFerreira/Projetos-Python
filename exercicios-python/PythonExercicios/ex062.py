print('Gerador de PA')
print('-=-'*10)
primeiro = int(input('Digite um valor: '))
razao = int(input('Digite a razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo} -> ', end='')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer calcular? '))
print('FIM')
print(f'Progressão finalizada com {total} termos mostrados.')
