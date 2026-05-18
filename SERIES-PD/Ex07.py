# A Series abaixo contém as notas finais (de 0 a 10) de alunos em uma disciplina. O índice é a matrícula do aluno:

# sNotas = pd.Series(
#     [4.5, 7.8, 9.1, 3.2, 6.5, 5.0, 8.8, 2.9, 7.0, 6.2],
#     index=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010]
# )
# a) Defina uma função conceito(nota) que retorne:
# 'A' se nota >= 9.0
# 'B' se nota >= 7.0
# 'C' se nota >= 5.0
# 'D' se nota < 5.0
# b) Aplique a função sobre sNotas usando .apply() e armazene em sConceitos.
# c) Quantos alunos ficaram em cada conceito? Exiba a tabela de frequências.
# d) Aplique uma segunda função que some 1.0 ponto apenas para notas menores que 5.0, sem ultrapassar 5.0. Salve como sNotasCorrigidas.
# e) Compare a média antes e depois da correção.

import pandas as pd
import numpy as np

sNotas = pd.Series(
    [4.5, 7.8, 9.1, 3.2, 6.5, 5.0, 8.8, 2.9, 7.0, 6.2],
    index=[1001,1002,1003,1004,1005,1006,1007,1008,1009,1010]
)

s_conceito = sNotas.apply(lambda x: 'A' if x>=9.0 else ('B' if x>=7.0 else('C' if x>=5.0 else 'D')))

qtd_conceitos = s_conceito.value_counts()

sNotasCorrigidas = sNotas.apply(
    lambda x: min(x + 1, 5.0) if x < 5.0 else x
    )

media_antes = sNotas.mean()
media_depois = sNotasCorrigidas.mean()

print("Quantos alunos ficaram em cada conceito? ",qtd_conceitos)
print("Aplique uma segunda função que some 1.0 ponto apenas para notas menores que 5.0, sem ultrapassar 5.0. ",sNotasCorrigidas)
print("Compare a média antes e depois da correção. ",media_antes, media_depois)