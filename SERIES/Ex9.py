import pandas as pd

estoque = {
    'Caneta':  {'Qtd': 120, 'Preço': 1.50, 'Mínimo': 20},
    'Caderno': {'Qtd': 45,  'Preço': 8.90},
    'Lápis':   {'Qtd': 200, 'Preço': 0.75, 'Mínimo': 50}
}

df_est = pd.DataFrame(estoque)

df_est_transposta = df_est.T



print(df_est.info())

