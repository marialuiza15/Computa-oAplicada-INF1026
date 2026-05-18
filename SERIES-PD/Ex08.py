# Dois supervisores registraram separadamente as horas trabalhadas por funcionários em uma semana. Alguns funcionários aparecem nos dois registros:

# sTurnoA = pd.Series(
#     [40, 36, 44, 38, 42],
#     index=['Ana','Bruno','Carla','Diego','Elena']
# )

# sTurnoB = pd.Series(
#     [35, 48, 36, 41, 39],
#     index=['Bruno','Felipe','Ana','Gabi','Carla']
# )
# a) Concatene as duas Series em uma única chamada sTotal usando pd.concat().
# b) Identifique os funcionários que aparecem mais de uma vez em sTotal.
# c) Para os funcionários duplicados, qual foi o total de horas trabalhadas (soma dos dois registros)?
# d) Atualize sTurnoA com os dados de sTurnoB usando .update(). O que acontece com os valores dos funcionários que existiam nos dois registros?
# e) Quantos funcionários no total (únicos) trabalharam? Use o Index para descobrir.

import pandas as pd
import numpy as np

sTurnoA = pd.Series(
    [40, 36, 44, 38, 42],
    index=['Ana','Bruno','Carla','Diego','Elena']
)

sTurnoB = pd.Series(
    [35, 48, 36, 41, 39],
    index=['Bruno','Felipe','Ana','Gabi','Carla']
)

sTotal  = pd.concat([sTurnoA, sTurnoB])

s_mais_de_1_vez = sTotal.value_counts().apply(lambda x: x>1)

s_duplicaods = sTotal.index.duplicated(keep=False) #pega os duplicatos 
s_duplicados_h_trab = sTotal[s_duplicaods].groupby(level=0).sum() #pega os duplicatos, agrupa e soma os values

sTurnoA.update(sTurnoB) #atualiza os valores de um com base no outro, ou seja, só atualiza valores que existem nos dois

s_funcionario = sTotal.index.unique()


print("Concatene as duas Series em uma única", sTotal)
print("Identifique os funcionários que aparecem mais de uma vez", s_mais_de_1_vez)
print("Para os funcionários duplicados, qual foi o total de horas trabalhadas", s_duplicados_h_trab)
print("Atualize sTurnoA com os dados de sTurnoB usando .update()", sTurnoA)
print("Quantos funcionários no total (únicos) trabalharam", s_funcionario)