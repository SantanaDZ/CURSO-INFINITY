nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1 + nota2 + nota3)/3

if media >= 6:
    print (f'Sua média é igual a {media}, você está aprovado!')
elif media >= 4 and media < 6:
    print (f'Sua média é igual a {media}, você está em recuperação!')
else:
    print(f'Sua média é igual a {media}, você está reprovado!')    
