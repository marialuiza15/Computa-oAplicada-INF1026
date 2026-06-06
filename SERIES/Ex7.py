import pandas as pd

dados = {
    'Nome':  ['Ana', 'Bruno', 'Carla', 'Diego'],
    'Nota1': [8.5, 6.0, 9.2, 7.1],
    'Nota2': [7.0, 8.5, 6.8, 9.0],
    'Nota3': [9.0, 5.5, 8.0, 7.5]
}

df_dados = pd.DataFrame(dados)

tam = df_dados.size
formato = df_dados.shape

top3 = df_dados.head(3)

resumo = df_dados.describe()

print(resumo)