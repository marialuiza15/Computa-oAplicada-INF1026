# Exercício Médio 1 — Classificação de notas de alunos

# Considere uma lista de alunos onde cada elemento é uma tupla no formato:
# (nome, nota1, nota2, nota3)

# Escreva uma função chamada classificar_alunos(lista_alunos) que:
# Receba uma lista de tuplas contendo os dados dos alunos.
# Calcule a média das três notas de cada aluno.

# Determine o status do aluno:
# "Aprovado" se a média for maior ou igual a 6.
# "Reprovado" caso contrário.

# Retorne uma tupla de tuplas, onde cada elemento contém:
# (nome, média, status)
# Exemplo de entrada
# [
#  ("Ana", 7.0, 6.5, 8.0),
#  ("João", 5.0, 4.5, 6.0),
#  ("Maria", 9.0, 8.5, 9.5)
# ]
# Exemplo de saída
# (
#  ("Ana", 7.16, "Aprovado"),
#  ("João", 5.16, "Reprovado"),
#  ("Maria", 9.0, "Aprovado")
# )

def classificar_alunos(lista_alunos):
    lista = []
    for aluno in lista_alunos:
        media = (aluno[1] + aluno[2] + aluno[3])/3
        nome = aluno[0]
        status = "Aprovado" if media >= 6 else "Reprovado"
        lista.append(tuple([nome, media, status]))
    return tuple(lista)


lista_alunos = [
 ("Ana", 7.0, 6.5, 8.0),
 ("João", 5.0, 4.5, 6.0),
 ("Maria", 9.0, 8.5, 9.5)
]

print(classificar_alunos(lista_alunos))