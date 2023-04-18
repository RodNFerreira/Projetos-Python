cont = num = soma = 0
num = int(input('Digite um valor [999 para parar] '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um valor [999 para parar] '))
print('Acabou.')
print(f'Você digitou {cont} números e soma entre eles foi {soma}.')
