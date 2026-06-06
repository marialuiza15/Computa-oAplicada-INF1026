import pandas as pd

s = pd.Series([23.0,22.4,10.0,15.0,12.0,25.0,18.5],index = ['seg','ter','qua','qui','sex','sab','dom'])

# iloc é para posicoes inteiras
# loc é para rotulo de texto

quarta = s.loc['qua']
semana = s.loc['sex':'dom'] #fatiamento
print(semana)