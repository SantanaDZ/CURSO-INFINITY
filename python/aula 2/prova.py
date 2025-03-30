# Criando a tupla com as equipes e suas notas

equipes = [
    ('Time Azul', [10, 20, 30]),
    ('Time Branco', [25, 30, 35]),
    ('Time Verde', [15, 25, 20]),
    ('Time Vermelho', [30, 40, 50])
]
print(equipes)

# Calculando a média de cada equipe 

medias = [(equipe[0], sum(equipe[1]) / len(equipe[1])) for equipe in equipes]

# Ordenar as médias em ordem decrescente

medias.sort(key=lambda x: x[1], reverse=False)

# Criar a lista de classificação
classificacao = medias

# Exibir a classificação final
print("Classificação Final:")
for i, (equipe, media) in enumerate(classificacao, start=1):
    print(f"{i}. {equipe}: {media:.2f}")