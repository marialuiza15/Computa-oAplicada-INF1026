# A Series abaixo registra as idades de participantes de uma pesquisa:

# sIdades = pd.Series(
#     [23, 45, 17, 62, 34, 28, 51, 19, 38, 72,
#      26, 44, 55, 31, 67, 22, 48, 15, 39, 58]
# )
# a) Use pd.cut() para categorizar as idades nas faixas etárias: jovem (0–25], adulto (25–50], idoso (50–inf). Use esses labels.

# b) Quantos participantes há em cada faixa etária? Use .value_counts() no resultado do cut.

# c) Exiba a frequência relativa (percentual) de cada faixa.

# d) Qual faixa etária possui a maior representação?

import pandas as pd
import numpy as np

sIdades = pd.Series(
    [23, 45, 17, 62, 34, 28, 51, 19, 38, 72,
     26, 44, 55, 31, 67, 22, 48, 15, 39, 58]
)

s_faixa1 = pd.cut(sIdades, bins=[0,25,50,np.inf], labels=['jovem', 'adulto','idoso'])  # vai gerar uma serie categorizando CADA valor da serie original
# bins → número de intervalos ou lista de cortes
# labels → nomes das categorias

s_qtd_fh = s_faixa1.value_counts()

freq_jovem = s_qtd_fh.loc['jovem']/sIdades.size
freq_adulto = s_qtd_fh.loc['adulto']/sIdades.size
freq_idoso = s_qtd_fh.loc['idoso']/sIdades.size

maior_rep_fh = s_qtd_fh.max()

print("Use pd.cut() para categorizar as idades nas faixas etárias: ", s_faixa1)
print("Quantos participantes há em cada faixa etária?: ", s_qtd_fh)
print("Exiba a frequência relativa (percentual) de cada faixa.: ")
print(freq_jovem)
print(freq_adulto)
print(freq_idoso)

print("Qual faixa etária possui a maior representação? ", maior_rep_fh)