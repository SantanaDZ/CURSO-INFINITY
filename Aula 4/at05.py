numeros = 0
pares = 0
for i in range(10):
    numeros= float(input("Digite um número: "))
    if numeros %2 == 0:
        pares +=1
print(f'O número de pares é igual a : {pares}')
