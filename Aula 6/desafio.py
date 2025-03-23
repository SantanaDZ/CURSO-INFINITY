import random
vendas = []

print('Bem-vindo ao sistema de vendas da Loja de Doces!')

while True:
    nome = input("Digite o nome do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    telefone = input("Digite o número de telefone do cliente: ")
    valor = float(input("Digite o valor da compra: R$ "))
    venda = {
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
        "valor": valor
    }
    vendas.append(venda)
    continuar = input("Deseja registrar outra venda? (s/n): ").lower()
    if continuar != 's':
        break
if vendas:
    sorteado = random.choice(vendas)
    print("\n***** FIM DO EXPEDIENTE *****")
    print(f"O cliente sorteado para ganhar um brinde foi: {sorteado['nome']}")
    print(f"Endereço: {sorteado['endereco']}")
    print(f"Telefone: {sorteado['telefone']}")
    print("Parabéns ao cliente!")
else:
    print("Nenhuma venda registrada no dia.")

print("Encerrando o sistema... Até amanhã!") 
input('')