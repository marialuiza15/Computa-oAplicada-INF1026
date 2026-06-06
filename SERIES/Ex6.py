import pandas as pd

s_cadastro = pd.Series( [0.5, 0.9, 1.0, 4.5, 2.1, 5.0, 8.9, 22.8], index=[210, 211, 212, 215, 233, 252, 232, 241] ) 
s_faltas = pd.Series( [3, 1, 0, 2, 5, 1, 4, 0], index=[210, 211, 212, 215, 233, 252, 232, 241] )

s_new = pd.Series([6.3], index=[233])

s_cadastro.update(s_new)

s_cadastro.loc[299]=12.0
s_faltas.loc[299]=7

def ve_funcionarios(f):
    if f>=5:
        return 'critico'
    else:
        return 'ok'
    
s_status = s_faltas.apply(ve_funcionarios)

limites = [0,3,10,float('inf')] # nao usar max(), é mais seguro usar float('inf')
titulos = ['perto', 'medio', 'longe']

s_faixa = pd.cut(s_cadastro, bins=limites, labels=titulos)

s_relatorio = pd.concat([s_cadastro,s_faltas,s_faixa,s_status], axis=1, keys=['distancia_km','faltas','faixa','status']) 

s_relatorio_filt = s_relatorio.loc[((s_faixa=='medio')| (s_faixa=='longe')) & (s_status=='critico')]

media_perto = s_relatorio.loc[s_faixa=='perto', 'faltas'].mean()
media_medio = s_relatorio.loc[s_faixa=='medio', 'faltas'].mean()
media_longe = s_relatorio.loc[s_faixa=='longe', 'faltas'].mean()

print(s_faixa)