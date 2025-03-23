# Tupla
# É uma sequencia de valores de qualquer tipo que não pode ser alterada.
#                0     1    2  
minha_tupla = ('Davi', 21, 1.72, True)

#Acessando valores
print(minha_tupla[0])

#Alterando (Não é possivel)
# minha_tupla[1] = 21

#Desempacotamento
nome, idade, altura, tem_pet = minha_tupla
print(nome)
print(idade)
print(altura)
print(tem_pet) 