import pandas as pd

dados = {210: 0.5, 211: 0.9, 212: 1.0, 213: 1.0, 215: 4.5}

s = pd.Series(dados)

s_novodado = pd.Series([3.2],index=[211])

s.update(s_novodado)

s.loc[220] = 7.8 #insere

print(s)