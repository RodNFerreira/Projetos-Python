while True:
    n = int(input('Quer ver a tabuada de qual número? '))
    print('-'*0)
    if n < 0:
        break
    for i in range(1, 11):
        print(f'{n} x {i} = {n*i}')
print('Programa de tabuada ENCERRADO! Volte sempre.')
