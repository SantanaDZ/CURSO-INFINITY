soma = 0
maior = float('-inf')
menor = float('inf')
qtd = 0
continuar = 'S'
while continuar == 'S':
    num = float(input('Digite o número: '))
    soma += num
    qtd += 1 
    if num > maior:
        maior = num
    elif num < menor:
        menor = num    

    continuar = input("Deseja continuar? [S/N]").strip().upper()
media = soma/qtd

print(f'''A quantidade de números é igual a: {qtd}' 
O menor número é igual a: {menor}
O maior número é igual a: {maior}
A soma é igual a: {soma}
A média é igual {media}
''')
