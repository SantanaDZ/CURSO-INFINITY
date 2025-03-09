maior = 0
print('Digite 5 números para retornar o maior')
for i in range (5):
    num = float(input(f'Digite o número {i+1}: '))
    if num > maior:
        maior = num
print(f'O maior número é: {maior}')         