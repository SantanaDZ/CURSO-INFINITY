num_certo = 7
contador = 0
print('----- JOGO DE ADIVINHAÇÃO -----')
print('* TRÊS TENTATIVAS PARA ADIVINHAR O NÚMERO *')
num_digitado = int(input('PRIMEIRA TENTATIVA, DIGITE UM NUMÉRO INTEIRO: '))
contador += 1
while num_certo != num_digitado and contador == 1:
    num_digitado = int(input('SEGUNDA TENTATIVA, DIGITE UM NÚMERO INTEIRO:  '))
    contador += 1
while num_certo != num_digitado and contador == 2:
    num_digitado = int(input('ÚLTIMA CHANCE, DIGITE UM NÚMERO INTEIRO:  '))
    contador +=1
if num_digitado == num_certo:
    print('PARABÉNS, VOCÊ ACERTOU! ')
else:
    print('QUE PENA, VOCÊ NÃO ACERTOU, TENTE NOVAMENTE')   

input()     


   
