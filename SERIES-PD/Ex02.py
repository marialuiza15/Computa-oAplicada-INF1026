# Dada a Series abaixo, que representa o estoque de produtos em uma loja:

# sEstoque = pd.Series(
#     [50, 30, 0, 120, 15],
#     index=['Caneta', 'Caderno', 'Borracha', 'Papel', 'Grampo']
# )
# a) Acesse o estoque de "Caderno" usando .loc.
# b) Acesse o segundo e quarto elementos usando .iloc.
# c) A "Borracha" recebeu 40 unidades. Atualize o valor.
# d) Um novo produto "Clips" chegou com 75 unidades. Inclua-o na Series.
# e) Exiba a Series final.

import pandas as pd

sEstoque = pd.Series(
    [50, 30, 0, 120, 15],
    index=['Caneta', 'Caderno', 'Borracha', 'Papel', 'Grampo']
)

s_estoque_caderno = sEstoque.loc['Caderno'] # localiza pelo indice
s_second_index = sEstoque.iloc[1] #localiza pela segunda posicao
s_fourth_index = sEstoque.iloc[3] #localiza pela quarta posicao
sEstoque.loc['Borracha'] += 40 #atualiza o valor, somando a ele 40 unidade
sEstoque.loc['Clips'] = 75 # insere o indice CLips na series e associa o valor 75 a ele.

print("Acesse o estoque de 'Caderno' usando .loc.: ", s_estoque_caderno)
print("Acesse o segundo elemento usando .iloc.: ", s_second_index)
print("Acesse o quarto elemento usando .iloc.: ", s_fourth_index)
print("A 'Borracha' recebeu 40 unidades. Atualize o valor.: ", sEstoque.loc['Borracha'])
print("Um novo produto 'Clips' chegou com 75 unidades. Inclua-o na Series.: ", sEstoque.loc['Clips'])
print("Exiba a Series final.: ", sEstoque)