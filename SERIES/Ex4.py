import pandas as pd

s_distancias = pd.Series([0.5, 0.9, 4.5, 8.9, 2.1, 22.8, 5.0], index=[210,211,215,232,233,241,252])

# o apply serve para aplicar uma função a cada elemento de uma series

def distancia(d):
    if d<=3:
        return 50.0
    elif d>3 and d<=10:
        return 150.0
    else:
        return 300.0
    
s_auxilio = s_distancias.apply(distancia)

s_auxilio_filt = s_auxilio.loc[s_auxilio==150]

total_gasto = s_auxilio.sum()

print(total_gasto)