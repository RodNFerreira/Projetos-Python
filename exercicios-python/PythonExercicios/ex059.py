from time import sleep
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
maior = 0
opcao = 0
while opcao != 5:
    print('''    [ 1 ] Somar
    [ 2 ] Multiplicar 
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] Sair do programa''')
    opcao = int(input('>>>>> Qual a opção? '))
    if opcao == 1:
        soma = valor1 + valor2
        print(f'A soma entre {valor1} e {valor2} resulta em {soma}.')
    elif opcao == 2:
        mult = valor1 * valor2
        print(f'A multiplicação entre {valor1} e {valor2} resulta em {mult}.')
    elif opcao == 3:
        if valor1 > valor2:
            maior = valor1
        else:
            maior = valor2
        print(f'O maior número entre {valor1} e {valor2} é {maior}.')
    elif opcao == 4:
        print('Informe os valores novamente!')
        valor1 = int(input('Digite o primeiro valor: '))
        valor2 = int(input('Digite o segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida! Tente novamente!')
    print('=-=' * 10)
    sleep(2)
    print('Fim do programa! Volte sempre!')



