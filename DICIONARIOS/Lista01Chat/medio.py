# Exercício Médio: Contagem de Ocorrências

# Enunciado:
# Crie um dicionário que conta o número de ocorrências de cada letra em uma string fornecida.
# Por exemplo, para a string "abracadabra", o dicionário resultante deve ser: {"a": 5, "b": 2, "r": 2, "c": 1, "d": 1}.

# Exemplo:
# # Teste
# resultado = contar_ocorrencias("abracadabra")
# print(resultado)

def contar_ocorrencias(palavra):
    cont = 0
    dict =  {}
    for letra in palavra:
    # verificar se a letrra esta no dicionatrio como chave, se estiver, adiciona 1 no valor correpondente
    # se nao, adiciona a nova chave e o valor 1.