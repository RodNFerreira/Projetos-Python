vel = float(input('Qual a velocidade atual do carro? '))
multa = (vel - 80) * 7
if vel > 80:
    print(f'MULTADO! Você estava acima da velocidade máxima de 80km/h! A multa será de R${multa:.2f}')
print('Tenha um bom dia! Dirija com segurança.')
