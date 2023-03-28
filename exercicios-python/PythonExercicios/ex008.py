medida = float(input('Uma distância em metros: '))
cm = medida*100
mm = medida*1000
dm = medida*10
dam = medida/10
hm = medida/100
km = medida/1000

print(f'A medida de {medida} metros corresponde a {cm} centímetros e {mm} milímetros.')
print(f'Já em decímetros, corresponde a {dm}, em decâmetros {dam}, em hectômetros {hm} e quilômetros, {km}.')
