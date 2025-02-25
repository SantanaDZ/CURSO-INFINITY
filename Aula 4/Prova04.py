inicio = int(input('Digite o início do intervalo: '))
final = int(input('Digite o final do intervalo: '))
soma = 0
for i in range (inicio,final+1):
    if i %2 == 0:
        soma += i
    
if soma >0:
    print(f'A soma dos números pares do intervalo é igual a : {soma}')
else: 
    print("Não há números pares no intervalo.")
input('')