# Faça um progrma em que peça 3 notas  no final a média entre elas
notas = []

# Preenchimento da Lista
for i in range(3):
    nota = float(input(f'Digite a {i+1}ª nota: '))
    notas.append(nota)

# Mostrar elementos da lista
# 1ª
# print ('Notas: ')
# for i in range(len(notas)):
#    print(f'-{notas[i]}')

# 2ª
for nota in notas:
    print(f'- {nota}')

media = sum(notas) / len(notas)

print(f'A média das notas é: {media}')