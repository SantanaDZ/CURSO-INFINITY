total_preco = 0
print('Digite o preço dos 5 produtos: ')
for i in range (5):
    preco_produto = float(input(f'Digite o preço do produto {i+1}: '))
    total_preco += preco_produto
    if total_preco > 100:
        desconto = total_preco * 0.1
        total_preco -= desconto
        print(f'O preço com desconto é igual a : {total_preco}')
        break
print(f'O preço total é igual a: {total_preco}')    