times = ('Botafogo', 'Fortaleza', 'Palmeiras', 'Internacional',
         'Fluminense', 'Cruzeiro', 'Grêmio', 'São Paulo',
         'Vasco da Gama', 'Atlético MG', 'Santos', 'Bragantino',
         'Flamengo', 'Atlético PR', 'Bahia', 'Goiás',
         'Corinthians', 'Cuiabá', 'Coritiba', 'América MG')
print('-='*15)
print(f'Lista  de times do Brasileirão: {times}.')
print('-='*15)
print(f'Os 5 primeiros colocados são {times[0:5]}.')
print(f'Os 4 últimos colocados são {times[-4:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O São Paulo está na {times.index("São Paulo")+1}° posição.')
