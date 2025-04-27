def processador_texto(texto, **kwargs):
    operacoes = {
        "contar_palavras": lambda txt: f"Número de palavras: {len(txt.split())}",
        "contar_letras": lambda txt: f"Número de letras (sem espaços): {len(''.join(txt.split()))}",
        "inverter_texto": lambda txt: txt[::-1],
        "substituir_palavra": lambda txt: txt.replace(kwargs.get("substituir_palavra", ""), kwargs.get("nova_palavra", ""))
    }

    resultado = texto
    for chave, operacao in kwargs.items():
        if chave in operacoes:
            resultado = operacoes[chave](resultado)

    return resultado


#TESTES
print("Olá mundo, tudo bem?")
print(processador_texto("Olá mundo, tudo bem?", contar_palavras=True))
print(processador_texto("Olá mundo, tudo bem?", contar_letras=True))
print(processador_texto("Olá mundo, tudo bem?", inverter_texto=True))
print(processador_texto("Olá mundo, tudo bem?", substituir_palavra="mundo", nova_palavra="pessoas"))