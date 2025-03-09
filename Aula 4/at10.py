positivos = 0
negativos = 0
print('Digite dez números de sua escolha: ')
for i in range(10):
    numeros= float(input(f"Digite o número {i+1}: "))
    if numeros > 0:
        positivos +=1

    elif numeros < 0:
        negativos +=1

    else:
        print('Número 0 digitado, loop encerado')
        break    
print(f'O número de positivos é igual a : {positivos}')
print(f'O número de negativos é igual a : {negativos}')
