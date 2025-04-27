# ENTRADA 


# PROCESSAMENTO 

# SAÍDA 

#========================================================================

def definePositivo(numero):
    resultado = ""
    if numero == 0:
        resultado = "Nulo"
    elif numero < 0:
        resultado = "Negativo"    
    else:
        resultado = "Positivo"
    return resultado    


print(definePositivo(-5))