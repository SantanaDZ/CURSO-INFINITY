qtd = int(input('Digite a quantidade de números a digitar: '))
soma = 0
for i in range(qtd):
    num = float(input(f'Número {i+1}: '))
    soma += num
media = soma/qtd
print(f'A média dos números é igual a {media} ')    
