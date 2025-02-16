contador = 0.0
soma_notas = 0.0
nota = 0.0

while nota != -1:
    nota = float(input("Digite a nota do aluno (ou -1 para encerrar): "))
    
    if nota != -1:
       soma_notas += nota
       contador += 1 
    
print(soma_notas, contador)
print('A média das notas é igual a : ', soma_notas/contador)

