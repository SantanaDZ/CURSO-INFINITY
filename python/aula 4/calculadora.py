def soma (a,b):
    return (a + b) 

def subtracao (a,b):
    return (a - b)

def produto (a,b):
    return (a * b) 

def divisao (a,b):
    if b == 0:
        return "Erro: divisão por zero."
    return (a / b) 

    

while True:
    print('--------- CALCULADORA ------------')
    
    print('Qual operação deseja realizar? ')
    print('1- Soma ')
    print('2- Subtração ')
    print('3- Multiplicação ')
    print('4- Divisão ')
    print('5- Sair ')
    opcao = input("Escolha uma opção (1 a 5): ")

    try:
        n1 = float(input('Digite o primeiro número '))
        n2 = float(input('Digite o segundo número '))
    except ValueError:
            print("Entrada inválida. Use apenas números.")
            continue    

    if opcao == '1':
        resultado = soma(n1,n2)
        print(f'A soma é igual a {resultado}')
    if opcao == '2':
        resultado = subtracao(n1,n2)
        print(f'A subtração é igual a {resultado}')
    if opcao == '3':
        resultado = produto(n1,n2)
        print(f'O produto é igual a {resultado}')
    if opcao == '4':
        resultado = divisao(n1,n2)
        print(f'A divisão é igual a {resultado}')
    if opcao == '5':
        print("Encerrando a calculadora. Até mais!")
        break
    if opcao not in ['1', '2', '3', '4']:
            print("Opção inválida. Tente novamente.")
            continue               
   