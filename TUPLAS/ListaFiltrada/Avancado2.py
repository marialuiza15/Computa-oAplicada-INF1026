# Exercício Difícil 2 — Análise de apostas da Mega-Sena

# As apostas de um sorteio da Mega-Sena estão armazenadas em duas tuplas paralelas:
# A primeira contém os nomes dos jogadores.
# A segunda contém as apostas correspondentes (tuplas de números).
# Cada aposta contém 6 números, mas não necessariamente está ordenada.

# Exemplo:
# tNomes = ('Kaka', 'Keko', 'Kiko', 'Kako', 'Kiko', 'Kaka', 'Keko', 'Kiko')
# tApostas = (
#  'Kaka',(1,2,6,44,49,59),
#  'Keko',(1,2,6,37,18,58),
#  'Kiko',(1,2,40,37,51,58),
#  'Kako',(6,3,18,49,45,57),
#  'Kaka',(6,2,25,37,38,39,42,54),
#  'Keko',(51,18,37,40,44,4),
#  'Kiko',(6,25,40,41,51,52,57),
#  (1,2,6,37,49,59)
# )
# O resultado do sorteio é representado por uma tupla de 6 números sorteados.

# Escreva uma função chamada maiorNumeroAcertos(tJogos, resultado) que:

# Receba uma tupla de jogos no formato:
# (nome, aposta)
# Compare cada aposta com o resultado do sorteio.
# Conte quantos números cada aposta acertou.

# Determine:
# o maior número de acertos obtido em uma aposta
# os nomes dos jogadores que tiveram essa quantidade de acertos (sem repetição)

# A função deve retornar uma tupla contendo:
# (maior_numero_de_acertos, (nomes_dos_jogadores))

def maiorNumeroAcertos(tJogos, resultado):
    qtdAcertos = 0
    listaAcertadores = []
    acertos = 0
    for jogo in tJogos:
        nome = jogo[0]
        acertos = 0
        for numero in jogo[1]:
            if numero in resultado:
                acertos+=1
        if acertos>qtdAcertos:
            qtdAcertos = acertos
            listaAcertadores.clear()
            listaAcertadores.append(nome)
        elif acertos == qtdAcertos and nome not in listaAcertadores:
            listaAcertadores.append(nome)
    return tuple([qtdAcertos, tuple(listaAcertadores)])
         
            
tupla= ( ('Kaka',(1,2,6,44,49,59)),
 ('Keko',(1,2,6,37,18,58)),
 ('Kiko',(1,2,40,37,51,58)),
 ('Kako',(6,3,18,49,45,57)),
 ('Kaka',(6,2,25,37,38,39,42,54)),
 ('Keko',(51,18,37,40,44,4)),
 ('Kiko',(6,25,40,41,51,52,57)))
print(maiorNumeroAcertos(tupla, (6,3,18,49,45,57)))