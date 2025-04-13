def calcular_imc (peso, altura):
    
    return peso / altura**2
    

peso = float(input('Digite o peso: '))
altura = float(input('Digite a altura: '))
imc = calcular_imc(peso,altura)
print(f'O IMC é igual a {imc}')

def classificar_imc(imc):
    if imc <= 18.5:
        return 'ABAIXO_DO_PESO'
    if 18.5 < imc <= 25:
        return 'PESO_IDEAL' 
    if 25 < imc <= 30:
        return 'SOBREPESO'
    if 30 < imc <= 35:
        return 'OBESIDADE_I'
    if 35 < imc <= 40:
        return 'OBESIDADE_II'
    if imc > 40:
        return 'OBESIDADE_III'
print(classificar_imc(imc))
    