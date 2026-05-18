# A Series abaixo registra as vendas diárias (em R$) de um vendedor ao longo de um mês. Os índices são os dias da semana em que ocorreram:

# sVendas = pd.Series(
#     [320, 85, 540, 210, 760, 95, 430, 310, 620, 150,
#      480, 70, 390, 820, 110, 560, 240, 730, 88, 410],
#     index=['Seg','Ter','Qua','Qui','Sex','Sab','Dom','Seg','Qua','Ter',
#            'Qui','Sab','Sex','Seg','Ter','Qua','Qui','Sex','Sab','Dom']
# )
# a) Filtre e exiba apenas as vendas superiores a R$ 500,00.
# b) Quantas vendas foram inferiores a R$ 100,00?
# c) Filtre as vendas que ocorreram às Segundas-feiras ('Seg').
# d) Quais foram as vendas entre R$ 200,00 e R$ 500,00 (inclusive)?
# e) Qual o percentual que as vendas acima de R$ 500 representam do total?

import pandas as pd

sVendas = pd.Series(
    [320, 85, 540, 210, 760, 95, 430, 310, 620, 150,
     480, 70, 390, 820, 110, 560, 240, 730, 88, 410],
    index=['Seg','Ter','Qua','Qui','Sex','Sab','Dom','Seg','Qua','Ter',
           'Qui','Sab','Sex','Seg','Ter','Qua','Qui','Sex','Sab','Dom']
)

s_vendas_sup_500 = sVendas.loc[sVendas>500]
vendas_inf_100 = sVendas.loc[sVendas<100].count()
s_vendas_seg = sVendas.loc['Seg']

s_vendas_entre_200_500 = sVendas.loc[(sVendas>=200) & (sVendas<=500)]
#s_vendas_entre_200_500 = sVendas.between(200,500)

perc_vend_sup_500 = s_vendas_sup_500.count() / sVendas.count()

print("Filtre e exiba apenas as vendas superiores a R$ 500,00.: ",s_vendas_sup_500)
print("Quantas vendas foram inferiores a R$ 100,00?: ",vendas_inf_100)
print("Filtre as vendas que ocorreram às Segundas-feiras ('Seg').: ",s_vendas_seg)
print("Quais foram as vendas entre R$ 200,00 e R$ 500,00 (inclusive)?: ",s_vendas_entre_200_500)
print("Qual o percentual que as vendas acima de R$ 500 representam do total?: ",perc_vend_sup_500)