impar = 0
pares = 0
for i in range(1,20+1):
    if i %2 == 0:
        pares +=1
    else:
        impar +=1
    while i == 15:
        print(f'Número 15 encontrado, loop encerrado. Número de pares = {pares}, número de ímpares = {impar} ')
        break
print(f'Número de pares até 20 = {pares}, número de ímpares até 20  = {impar} ')
        