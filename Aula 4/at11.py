# maior_que_20 = 'Não'
# multiplo_de_5 ='Não'
# for i in range (1,31):
#     print(i)
#     if i % 5 == 0:
#         multiplo_de_5 = 'Sim'
#     elif i > 20:
#         maior_que_20 = 'Sim'        
#     print(f'Múltiplo de 5: {multiplo_de_5}, maior que 20: {maior_que_20}' )       

for i in range(1, 31):
    # Verifica se o número é múltiplo de 5
    if i % 5 == 0:
        print(f"{i} é múltiplo de 5")
    
    # Verifica se o número é maior que 20 e interrompe o loop
    if i > 20:
        print(f"{i} é maior que 20, interrompendo o loop")
        break
    
    print(i)