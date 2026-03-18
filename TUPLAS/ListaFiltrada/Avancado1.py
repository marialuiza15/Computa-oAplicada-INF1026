# Exercício Difícil 1 — Compressão de texto (Run-Length Encoding)

# Escreva uma função chamada comprimir_texto(texto) que:
# Receba uma string.
# Analise a sequência de caracteres da string.
# Agrupe caracteres consecutivos iguais.

# Retorne uma tupla de tuplas, onde cada tupla contém:
# (caractere, quantidade_de_repetições_consecutivas)

# Exemplo

# Entrada:
# "aaabbc"

# Saída:
# (('a',3), ('b',2), ('c',1))

# Outro exemplo:

# Entrada:
# "hellooo!!"

# Saída:
# (('h',1), ('e',1), ('l',2), ('o',3), ('!',2))


def comprimir_texto(texto):
    listaStr=[]
    listaFreq=[]
    listaOut =[]
    for caracter in texto:
        if caracter not in listaStr:
            listaStr.append(caracter)
            listaFreq.append(1)
        else:
            pos = listaStr.index(caracter)
            listaFreq[pos] += 1
    
    for i in range(len(listaStr)):
        tupla = (listaStr[i], listaFreq[i])
        listaOut.append(tupla)

    return tuple(listaOut)

print(comprimir_texto("hellooo"))