notas = 0
media = 0
soma = 0
for i in range (1, 6):
    notas = float(input(f'Digite a nota {i}: '))
    soma+= notas
media = soma/5
print(media)