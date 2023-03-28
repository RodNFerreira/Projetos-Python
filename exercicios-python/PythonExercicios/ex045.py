from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra 
[ 1 ] Papel 
[ 2 ] Tesoura''')
jogador = int(input('Qual a sua escolha? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)
if computador == 0:  # Computador jogou pedra
    if jogador == 0:
        print('EMPATE!!!')
    elif jogador == 1:
        print('PARABÉNS! O JOGADOR VENCEU!')
    elif jogador == 2:
        print('O COMPUTADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 1:  # Computador jogou papel
    if jogador == 0:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 1:
        print('EMPATE!!!')
    elif jogador == 2:
        print('PARABÉNS! O JOGADOR VENCEU!')
    else:
        print('JOGADA INVÁLIDA!')

elif computador == 2:  # Computador jogou tesoura
    if jogador == 0:
        print('PARABÉNS! O JOGADOR VENCEU!')
    elif jogador == 1:
        print('O COMPUTADOR VENCEU!')
    elif jogador == 2:
        print('EMPATE!!!')
    else:
        print('JOGADA INVÁLIDA!')
