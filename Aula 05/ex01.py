print('Digite três números para somar: ')
soma = 0
for i in range(3):
    num = float(input(f'Número {i+1}: '))
    soma += num
print(f'A soma é igual a {soma} ')    