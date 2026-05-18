# Você recebeu a Series abaixo com dados de temperatura (°C) registrados em diferentes cidades. Alguns sensores falharam e geraram valores ausentes:

# sTemp = pd.Series(
#     [28.5, None, 31.0, 22.0, None, 35.5, 19.8, 31.0, 27.3, None, 24.6],
#     index=['Rio','SP','Brasília','Curitiba','Manaus','Fortaleza',
#            'Porto Alegre','Recife','Salvador','Belém','Belo Horizonte']
# )
# a) Identifique quais cidades possuem valores ausentes.
# b) Remova os valores ausentes e salve em uma nova Series sTemp_limpa.
# c) Ordene sTemp_limpa pelos valores de temperatura em ordem decrescente.
# d) Quantas temperaturas únicas existem na Series limpa?
# e) Remova as cidades "Curitiba" e "Recife" da Series limpa (use .drop()).

import pandas as pd

sTemp = pd.Series(
    [28.5, None, 31.0, 22.0, None, 35.5, 19.8, 31.0, 27.3, None, 24.6],
    index=['Rio','SP','Brasília','Curitiba','Manaus','Fortaleza',
           'Porto Alegre','Recife','Salvador','Belém','Belo Horizonte']
)

s_cidades_ausentes = sTemp.isnull() # lista com true e falso oq é e nao é null
sTemp_limpa = sTemp.dropna() # cria nova series sem os valores null
s_ordenado = sTemp_limpa.sort_values()
qtd_temps_unicas = sTemp.nunique() #conta quantos valores únicos (distintos) existem.
sTemp_limpa.drop('Curitiba', inplace= True) #assim modifica direto, sem o inplace vai gerar nova serie
sTemp_limpa.drop('Recife', inplace= True)

print("Identifique quais cidades possuem valores ausentes: ", s_cidades_ausentes)
print("Remova os valores ausentes e salve em uma nova Series sTemp_limpa.: ", sTemp_limpa)
print("Ordene sTemp_limpa pelos valores de temperatura em ordem decrescente. ", s_ordenado)
print("Quantas temperaturas únicas existem na Series limpa?: ", qtd_temps_unicas)
print("Remova as cidades Curitiba e Recife da Series limpa: ", sTemp_limpa)