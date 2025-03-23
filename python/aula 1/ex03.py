
numeros = []
for i in range(6):
    num= int(input(f'Digite o {i+1}º número: '))
    numeros.append(num)
print(f'A lista de números digitados foi : {numeros}')
soma = sum(numeros)
print(soma)