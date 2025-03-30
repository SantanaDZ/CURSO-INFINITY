aluno = {}
notas = []

aluno['nome'] = input('Digite o nome do aluno: ')
for i in range (3):
    nota = float(input(f'Digite a {i+1}ª nota: '))
    notas.append(nota)

aluno['notas'] = notas


aluno['media'] = sum(notas)/ len(notas)
if aluno['media'] >= 6:
    aluno['situacao'] = 'Aprovado'
else:
    aluno['situacao'] = 'Reprovado'

print('Aluno: ')
print(f'Nome: {aluno['nome']}')
print(f'Notas: {aluno.get('notas')}')
print(f'Média: {aluno.get('media')}')
print(f'Situação: {aluno.get('situacao')}')