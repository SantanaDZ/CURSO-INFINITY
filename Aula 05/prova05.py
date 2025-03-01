situacao = ''
soma_turma = 0
num_alunos = int(input('Digite o número de alunos da turma: '))
for i in range (num_alunos):
    nome = input('Digite o nome do aluno: ')
    nota1 = float(input('Digite o valor da nota 1: '))
    nota2 = float(input('Digite o valor da nota 2: '))
    nota3 = float(input('Digite o valor da nota 3: '))    
    media = (nota1 + nota2 + nota3)/3
    soma_turma += media
    if media >= 7:
        situacao = 'Aprovado'
    else:
        situacao = 'Reprovado'    
    print(f'As notas de {nome} foram: {nota1}, {nota2} e {nota3}. A média das notas foi {media}. {nome} está {situacao}')
media_geral =  soma_turma/num_alunos
print(f'A média geral da turma foi : {media_geral}') 
input('')
       

        