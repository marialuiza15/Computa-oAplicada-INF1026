import pandas as pd

notas = {
    'Ana':   {'P1': 8.5, 'P2': 7.0, 'P3': 9.0},
    'Bruno': {'P1': 6.0, 'P2': 8.5, 'P3': 5.5},
    'Carla': {'P1': 9.2, 'P2': 6.8, 'P3': 8.0},
    'Diego': {'P1': 7.1, 'P2': 9.0, 'P3': 7.5}
}

matriculas = {
    'Bruno': {'Matr': 101, 'Turma': 'A'},
    'Diego': {'Matr': 102, 'Turma': 'B'},
    'Carla': {'Matr': 103, 'Turma': 'A'},
    'Elisa': {'Matr': 104, 'Turma': 'B'}
}

df_notas = pd.DataFrame(notas)
df_mat = pd.DataFrame(matriculas)

df_geral = pd.concat([df_notas, df_mat], axis=0)

print(df_geral.shape)