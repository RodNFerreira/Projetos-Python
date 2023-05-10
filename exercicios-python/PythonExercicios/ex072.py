cont = ('zero', 'um', 'dois', 'três', 'quatro',
        'cinco', 'seis', 'sete', 'oito', 'nove',
        'dez', 'onze', 'doze', 'treze', 'catorze',
        'quinze', 'dezesseis', 'dezessete', 'dezoito',
        'dezenove', 'vinte')
while True:
    num = int(input('Digite um número de 0 a 20: '))
    if num < 0 or num > 20:
        print('Tente novamente. ', end='')
    else:
        print(f'Você digitou o número {cont[num]}.')
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N] '))
    if resp == 'N':
        break
print('FIM DO PROGRAMA!')
