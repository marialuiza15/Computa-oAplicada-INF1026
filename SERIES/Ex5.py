import pandas as pd

turma_a = pd.Series([8.5, 6.0, 9.2, 4.8], index=['Ana','Bruno','Carla','Diego'])
turma_b = pd.Series([7.3, 5.5, 10.0, 3.2], index=['Eva','Fabio','Gia','Hugo'])

s_turma_total = pd.concat([turma_a, turma_b])

limites = [0,5,7,9,10]
titulos = ['Reprovado', 'Regular', 'Bom', 'Excelente']

s_conceitos = pd.cut(s_turma_total, bins=limites, labels=titulos)

turma_total = pd.concat([s_turma_total,s_conceitos], axis=1) 
# axis=0 ele coloca a segunda series ABAIXO da primeira
# axis=1 ele coloca a segunda series AO LADO da primeira

print(turma_total)