preco = float(input('Qual o preço do produto? R$'))
novo = preco - (preco * 5 / 100)
print(f'O preço do produto, com o desconto de 5%, fica em um total de: R${novo:.2f}')

