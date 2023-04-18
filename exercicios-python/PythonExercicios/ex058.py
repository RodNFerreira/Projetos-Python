from random import randint
computador = randint(0, 10)
print('Sou seu computador! Acabei de pensar em um número entre 1 e 10...')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos! Tente outra vez! ')
        if jogador < computador:
            print('Mais! Tente outra vez! ')

print(f'Acertou! Foram necessários {palpites} palpites.')
