def multiplicar (a,b):
    return (a * b) 

def main():
    n1 = int(input('Digite o primeiro número '))
    n2 = int(input('Digite o segundo número '))

    resultado = multiplicar(n1,n2)
    print(f'{n1} X {n2} = {resultado}')

main()    