from random import randint
v = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = '  '
    while tipo not in 'PpIi':
        tipo = str(input('Par ou ímpar? [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}.')
    print('Deu PAR!' if total % 2 == 0 else 'Deu ÍMPAR!')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            v += 1
        else:
            print('Você PERDEU!')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            v =+ 1
        else:
            print('Você PERDEU!')
            break
        print('Vamos jogar novamente...')
print(f'GAME OVER! VOCÊ VENCEU {v} VEZES.')
