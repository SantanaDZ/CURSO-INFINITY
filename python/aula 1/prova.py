# Gerenciamento de Compras de Produtos

# Você foi contratado para desenvolver um programa que auxiliará no processo de compra de produtos em uma loja.
# O programa deve permitir que o usuário insira o nome e o preço de diversos produtos, 
# e após a inserção de cada produto, deve perguntar se o usuário deseja adicionar mais produtos à lista. 
# O processo de inserção de produtos continuará até que o usuário opte por parar.

# Ao término das inserções, o programa deve fornecer um resumo da compra com as seguintes informações:

# A) Total gasto na compra: O programa deve calcular e exibir a soma de todos os preços dos produtos inseridos.

# B) Quantidade de produtos que custam mais de R$1000: O programa deve contar e exibir quantos dos produtos cadastrados têm preço superior a R$1000.

# C) Nome do produto mais barato: O programa deve identificar e exibir o nome do produto com o menor preço.

produtos = []  
total_gasto = 0 
produtos_acima_1000 = 0  
produto_mais_barato = None 

while True:
    nome_produto = input("Digite o nome do produto: ")
    preco_produto = float(input(f"Digite o preço de {nome_produto}: R$"))
    produtos.append((nome_produto, preco_produto))
    total_gasto += preco_produto

    if preco_produto > 1000:
        produtos_acima_1000 +=1

    if produto_mais_barato is None or preco_produto < produto_mais_barato[1]:
        produto_mais_barato = (nome_produto, preco_produto)

    continuar = input("Deseja adicionar mais produtos? (s/n): ").strip().lower()
    if continuar != 's':
            break    
print("\nResumo da Compra:")
print(f"Total gasto: R${total_gasto:.2f}")
print(f"Quantidade de produtos acima de R$1000: {produtos_acima_1000}")
if produto_mais_barato:
    print(f"Produto mais barato: {produto_mais_barato[0]} (R${produto_mais_barato[1]:.2f})")


