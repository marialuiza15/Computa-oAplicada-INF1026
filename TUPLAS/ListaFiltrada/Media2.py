# Exercício Médio 2 — Ranking de vendas

# Considere uma lista de vendedores, onde cada elemento é uma tupla no formato:
# (nome, total_vendas)

# Escreva uma função chamada melhor_vendedor(vendas) que:
# Receba uma lista de tuplas com os vendedores e seus totais de vendas.
# Determine qual vendedor possui o maior valor de vendas.
# Retorne o nome do vendedor com maior total de vendas.

# Exemplo de entrada
# [("Carlos", 1500), ("Ana", 2300), ("João", 1800)]
# Exemplo de saída
# Ana

def melhor_vendedor(vendas):
    maior = 0
    melhorvendedor = ''
    for vendedor in vendas:
        if vendedor[1]>maior:
            melhorvendedor = vendedor[0]
            maior = vendedor[1]

    return melhorvendedor

print(melhor_vendedor([("Carlos", 1500), ("Ana", 2300), ("João", 1800)]))