def media (notas):
    return sum(notas)/len(notas)
notas =[]
while True:
    nota = float(input('Digite o valor da nota '))
    notas.append(nota)
    op = input('Deseja continuar adicionando notas? (S/N)').lower()
    if op == 'n':
        break




resultado = media(notas)
print(resultado)