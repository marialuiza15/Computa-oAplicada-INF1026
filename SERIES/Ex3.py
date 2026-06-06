import pandas as pd

dados = {'Ana': 8.5, 'Bruno': 6.0, 'Carla': 9.2, 'Diego': 4.8, 'Eva': 7.3}

s = pd.Series(dados)

media = s.mean()
maximo = s.max()
em_ordem = s.sort_values()

s_filt = s.loc[s>7.0] # esse filtro nao modifica a series, entao é preciso atribuir a uma nova variavel

print(s_filt)