idade= int(input('Digite sua idade: '))
if idade < 16:
    print('Você não pode votar.')
elif idade >= 16 and idade < 18:
    print('Você pode votar.')    
elif idade >= 18 and idade < 65:
    print('Seu voto é obrigatório.') 
else:
    print('Seu voto é facultativo')      