import pandas as pd

# Dados fictícios
dados = [
    {"ano": 2021, "fazenda": "Fazenda A", "milho": 100, "soja": 150, "trigo": 80},
    {"ano": 2021, "fazenda": "Fazenda B", "milho": 120, "soja": 130, "trigo": 90},
    {"ano": 2021, "fazenda": "Fazenda C", "milho": 110, "soja": 140, "trigo": 100},

    {"ano": 2022, "fazenda": "Fazenda A", "milho": 105, "soja": 160, "trigo": 85},
    {"ano": 2022, "fazenda": "Fazenda B", "milho": 125, "soja": 135, "trigo": 95},
    {"ano": 2022, "fazenda": "Fazenda C", "milho": 115, "soja": 145, "trigo": 105},

    {"ano": 2023, "fazenda": "Fazenda A", "milho": 110, "soja": 155, "trigo": 90},
    {"ano": 2023, "fazenda": "Fazenda B", "milho": 130, "soja": 140, "trigo": 100},
    {"ano": 2023, "fazenda": "Fazenda C", "milho": 120, "soja": 150, "trigo": 110},
]

# Criar DataFrame
df = pd.DataFrame(dados)
df["total"] = df[["milho", "soja", "trigo"]].sum(axis=1)

# A) Ano com produção total máxima e mínima
producao_ano = df.groupby("ano")["total"].sum()
ano_max = producao_ano.idxmax()
ano_min = producao_ano.idxmin()

print("📅 Produção total por ano:\n", producao_ano)
print(f"\n✅ Ano com maior produção: {ano_max} ({producao_ano[ano_max]} toneladas)")
print(f"✅ Ano com menor produção: {ano_min} ({producao_ano[ano_min]} toneladas)")

# B) Cultura com maior e menor produção total
producao_cultura = df[["milho", "soja", "trigo"]].sum()
cultura_max = producao_cultura.idxmax()
cultura_min = producao_cultura.idxmin()

print("\n🌱 Produção total por cultura:\n", producao_cultura)
print(f"\n✅ Cultura com maior produção: {cultura_max} ({producao_cultura[cultura_max]} toneladas)")
print(f"✅ Cultura com menor produção: {cultura_min} ({producao_cultura[cultura_min]} toneladas)")

# C) Fazenda com produção máxima e mínima em um ano específico
ano_escolhido = 2022
df_ano = df[df["ano"] == ano_escolhido]
fazenda_max = df_ano.loc[df_ano["total"].idxmax()]
fazenda_min = df_ano.loc[df_ano["total"].idxmin()]

print(f"\n🏡 Produção por fazenda no ano {ano_escolhido}:\n", df_ano[["fazenda", "total"]])
print(f"\n✅ Fazenda com maior produção: {fazenda_max['fazenda']} ({fazenda_max['total']} toneladas)")
print(f"✅ Fazenda com menor produção: {fazenda_min['fazenda']} ({fazenda_min['total']} toneladas)")
