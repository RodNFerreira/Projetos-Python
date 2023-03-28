from random import randint
from time import sleep
computador = randint(0, 5)  # Faz o computador "PENSAR"
print('-=-' * 20)
print('Estou pensando em um número entre 0 e 5, tente adivinhar!')
print('-=-' * 20)
jogador = int(input('Digite um número: '))  # Jogador tenta adivinhar
print('Processando...')
sleep(2)
if jogador == computador:
    print('Correto! você venceu!')
else:
    print(f'Errado! Eu pensei no {computador} e não no {jogador}! Eu venci!')
