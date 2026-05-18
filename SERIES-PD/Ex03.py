# A Series abaixo contém os preços de produtos em um mercado:

# sPrecos = pd.Series(
#     [5.99, 12.50, 3.75, 8.20, 15.00, 3.75, 9.40, 6.80],
#     index=['Pão','Frango','Sal','Arroz','Carne','Feijão','Macarrão','Azeite']
# )
# Calcule e exiba:

# a) Média, mediana e moda dos preços.
# b) O produto mais caro e o mais barato (valor e nome).
# c) Desvio padrão e variância.
# d) O resumo estatístico completo com .describe().

import pandas as pd

sPrecos = pd.Series(
    [5.99, 12.50, 3.75, 8.20, 15.00, 3.75, 9.40, 6.80],
    index=['Pão','Frango','Sal','Arroz','Carne','Feijão','Macarrão','Azeite']
)

s_media = sPrecos.mean() #calcula a media
s_mediana= sPrecos.median() #calcula a mediana
s_moda = sPrecos.mode() #calcula a moda

s_max = sPrecos.max() #obtem o VALOR  maximo/maior
s_min = sPrecos.min() #obtem o VALOR minimo/menor

s_rotulo_maxvalue = sPrecos.idxmax() #obtem o ROTULO DO VALOR maximo/maior
s_rotulo_minvalue = sPrecos.idxmin() #obtem o ROTULO DO VALOR minimo/menor

s_desvio_padrao = sPrecos.std() #Calcula o desvio padrão

'''
Desvio pádrao: 

Mede o quanto os valores estão espalhados em relação à média

Baixo desvio padrão → valores próximos da média
Alto desvio padrão → valores muito dispersos

'''

s_descricao = sPrecos.describe() #resumos estatisticos

print("Média dos preços: ",s_media)
print("Mediana dos preços: ",s_mediana)
print("Moda dos preços: ",s_moda)
print("O produto mais caro (valor e nome).: ",s_max, s_rotulo_maxvalue)
print("O produto mais barato  (valor e nome).: ",s_min, s_rotulo_minvalue)
print("Desvio padrão e variância.: ",s_desvio_padrao)
print("O resumo estatístico completo: ",s_descricao)