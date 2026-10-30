# Abre o arquivo como texto normal para dar uma espiada
# with open("pesquisa_saude.csv", "r", encoding="utf-8", errors="ignore") as arquivo:
#     print("--- 5 PRIMEIRAS LINHAS DO ARQUIVO ---")
#     for i in range(5):
#         print(arquivo.readline())

import pandas as pd
# 1. Indicamos que o separador é a barra vertical |
# 2. Mudamos o 'engine' para python para ele lidar melhor com os textos gigantes dos resumos

# Adicionamos o encoding="latin-1" para ele aceitar os acentos e cedilhas
dados = pd.read_csv("pesquisa_saude.csv", sep="|", engine="python", encoding="latin-1")

print("--- DADOS CARREGADOS COM SUCESSO! ---")
print(dados.head(2))  # Mostra apenas as 2 primeiras linhas para não inundar a tela

print("\n--- FORMATO DA TABELA (LINHAS, COLUNAS) ---")
print(dados.shape)

print("\n--- QUANTIDADE DE PESQUISAS POR ESTADO ---")
print(dados["uf_pesquisa"].value_counts())

print("\n--- TOTAL GASTO EM BOLSAS (R$) ---")
print(dados["valor_bolsa"].sum())

print("\n--- EDITAIS MAIS COMUNS ---")
print(dados["nome_edital_contrato"].value_counts().head(5))