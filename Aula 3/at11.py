'''num = int(input('Digite um número de 1 a 10: '))
if num >= 1 and num <= 10:
    print('Obrigado.')
else:    
    num = int(input)('Digite um número de 1 a 10: ')
    if num >= 1 and num <= 10:
        print('Obrigado!')'''

while True:
    try:
        numero = int(input("Digite um número entre 1 e 10: "))
        if 1 <= numero <= 10:
            print("Número válido fornecido:", numero)
            break
        else:
            print("Por favor, digite um número dentro do intervalo especificado.")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")
       
    
   
