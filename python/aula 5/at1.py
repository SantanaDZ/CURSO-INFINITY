def Calcula_Media(soma,qtd):
    return soma/qtd
soma = 0
qtd = 0
for i in range (3):
    nota =float(input(f'Digite a nota {i+1}: '))
    soma += nota
    qtd += 1
media = Calcula_Media(soma,qtd)    
print (f'A média é igual a: {media}')

