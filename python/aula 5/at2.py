def Calcular_Area_Retangulo(comprimento, altura):
    return comprimento * altura
comprimento = float(input('Digite o comprimento do retângulo: '))
altura = float(input('Digite a altura do retângulo: '))

area = Calcular_Area_Retangulo(comprimento, altura)
print(f'A Àrea do retângulo é igual a {area} m²')