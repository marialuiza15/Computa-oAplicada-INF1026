# Crie uma Series chamada sNotas com as notas de 6 alunos, usando os nomes dos alunos como índice:

# Ana: 8.5,  Bruno: 6.0,  Carla: 9.2,
# Diego: 7.5,  Elena: 5.0,  Felipe: 8.0
# Em seguida, responda utilizando código Python:

# a) Quantos elementos a Series possui?
# b) Quais são os labels do índice?
# c) Quais são os valores armazenados?
# d) Exiba os 3 primeiros e os 2 últimos elementos.

import pandas as pd

d = {'Ana': 8.5,  'Bruno': 6.0,  'Carla': 9.2,'Diego': 7.5,  'Elena': 5.0,  'Felipe': 8.0}

sr = pd.Series(d)

qtd_elem_sr = sr.size # Qtd de elementos
label_indice_sr = sr.index  # mostra os indices
valores_sr = sr.values # mostra os valores, a formatação vem bugada por natureza dio numpy. Para tratar bonito é preciso converter para lista ao exibir - .tolist()
three_firsts = sr.head(3) # mostra os 3 primeiros
two_lasts = sr.tail(2) # mostra os 2 ultimos

print("Quantos elementos a Series possui?: ", qtd_elem_sr)
print("Quais são os labels do índice?: ", label_indice_sr)
print("Quais são os valores armazenados?: ", valores_sr)
print("Exiba os 3 primeiros elementos.: ", three_firsts)
print("Exiba os 2 últimos elementos.: ", two_lasts)
