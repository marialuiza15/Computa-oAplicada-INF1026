import pandas as pd

dados = {
    'Nome':  ['Ana', 'Bruno', 'Carla', 'Diego'],
    'Nota1': [8.5, 6.0, 9.2, 7.1],
    'Nota2': [7.0, 8.5, 6.8, 9.0],
    'Nota3': [9.0, 5.5, 8.0, 7.5]
}

df_dados = pd.DataFrame(dados)

df_dados = df_dados.set_index('Nome')

df_dados = df_dados.rename(columns={'Nota1':'P1','Nota2':'P2','Nota3':'P3'})

label_indice = df_dados.index
label_columns = df_dados.columns

df_dados = df_dados.rename_axis(['Aluno'], axis=0)

print(df_dados)


# rename_axis da nome a linha das colunas da tabela por 4exemplo
# rename muda o nome de uma coluna

# o Pandas não altera o original a nao ser q use o argumento inplace=True.