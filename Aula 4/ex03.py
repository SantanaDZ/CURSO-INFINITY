inicio = int(input('Digite o início da contagem: '))
final = int(input('Digite o final da contagem: '))
passo = int(input('Digite o passo da contagem: '))

for i in range (inicio,final+1, passo):
    inicio += passo
    print(i)