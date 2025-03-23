ant = 0
suc = 1

print("Sequência de Fibonacci")
n = int(input('Digite até qual N termo você deseja mostrar a sequência:  '))

for _ in range(n):
    print(ant,end=" ")
    ant, suc = (suc, ant + suc)

print('\n')     