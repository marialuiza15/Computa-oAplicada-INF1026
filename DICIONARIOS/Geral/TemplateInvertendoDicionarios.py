# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 09:59:34 2026

@author: Ferlin
"""

# -*- coding: utf-8 -*-
"""
================================================================================
SISTEMA DE ANÁLISE GAMER 2026
================================================================================
Template de Exercícios - Dicionários Encadeados e Processamento de Dados

INSTRUÇÕES:
1. Complete todas as funções marcadas com "# COMPLETAR"
2. Execute o código para testar suas soluções
3. Compare os resultados com os esperados

OBJETIVOS:
- Transformar dados espalhados em um dicionário master
- Realizar junções (joins) entre múltiplos dicionários
- Inverter dicionários para responder perguntas
- Calcular frequências e agrupar dados

AUTOR: [Seu nome]
DATA: [Data]
================================================================================
"""

# ==============================================================================
# PARTE 1: DADOS INICIAIS (JÁ FORNECIDOS - NÃO ALTERAR)
# ==============================================================================

# Dicionário: ID do Jogador → (ID do Jogo, Rank)
d_jogadores = {
    10: ('LOL', 'Diamante'),
    20: ('VAL', 'Imortal'),
    30: ('LOL', 'Ouro'),
    40: ('FIFA', 'Elite'),
    50: ('VAL', 'Radiante'),
    60: ('CS2', 'Global')
}

# # Dicionário: ID do Jogo → (Nome do Jogo, ID do Estúdio)
d_jogos = {
    'LOL': ('League of Legends', 'RIOT'),
    'VAL': ('Valorant', 'RIOT'),
    'CS2': ('Counter-Strike 2', 'VALVE')
}

# # Dicionário: ID do Estúdio → (Nome do Estúdio, ID da Plataforma)
d_estudios = {
    'RIOT': ('Riot Games', 'PC'),
    'VALVE': ('Valve Corp', 'STEAM')
}

# # Dicionário: ID da Plataforma → (Nome da Plataforma, Empresa)
d_plataformas = {
    'PC': ('Computador', 'Diversos'),
    'STEAM': ('Steam Deck', 'Valve')
}

# # Dicionário: ID do Jogador → Nickname
d_nomes = {
    10: "Shadow",
    20: "Viper",
    30: "Pingu",
    40: "Goleiro",
    50: "Ace",
    60: "Sniper"
}


# ==============================================================================
# PARTE 2: FUNÇÕES PARA COMPLETAR
# ==============================================================================

# ------------------------------------------------------------------------------
# 2.1) TRANSFORMAÇÃO: DICIONÁRIO DE DICIONÁRIOS (MASTER)
# ------------------------------------------------------------------------------
def criar_master_dict(jogadores, jogos, estudios, plataformas, nomes):
    """
    OBJETIVO: Transformar todos os dados em uma única estrutura aninhada (Master).
    
    RECEBE:
        nomes      (dict): dicionário com ID jogador → nickname
        jogadores  (dict): dicionário com ID do jogador → (ID jogo, rank)
        jogos      (dict): dicionário com ID jogo → (nome, ID estúdio)
        estudios   (dict): dicionário com ID estúdio → (nome, ID plataforma)
        plataformas(dict): dicionário com ID plataforma → (nome, empresa)
        
    
    RETORNA:
        dict: dicionário onde cada chave é ID do jogador e o valor é um dicionário
              com os campos: "nickname", "jogo", "rank", "estudio", "plataforma"
    
    DICA: Use .get() para acessar valores com segurança (evitar erros)
    """
    master ={}

    # FORMA COMO FIZ ANTES
    # for (idJogador,nickname) in nomes.items():
    #     if idJogador in jogadores.keys():
    #         idJogo, rank = jogadores.get(idJogador)
    #         if idJogo in jogos.keys():
    #             nomeJogo, idStudio = jogos.get(idJogo)
    #             if idStudio in estudios.keys():
    #                 nomeStudio, idPlataforma = estudios.get(idStudio)
    #                 if idPlataforma in plataformas.keys():
    #                     nomePlataforma, empres = plataformas.get(idPlataforma)
    #                     master.update({
    #                         idJogador: {"nickname": nickname, "jogo": nomeJogo, "rank": rank, "estudio": nomeStudio, "plataforma": nomePlataforma}
    #                     })

    for (idJogador, nickname) in nomes.items():

        tdados_jogadores = jogadores.get(idJogador, ("?","?"))
        idJogo, rank = tdados_jogadores

        tdados_jogos = jogos.get(idJogo, ("?","?"))
        nomeJogo, idStudio = tdados_jogos
        
        tdados_estudios = estudios.get(idStudio, ("?","?"))
        nomeStudio, idPlataforma = tdados_estudios

        tdados_plataformas = plataformas.get(idPlataforma, ("?","?"))
        nomePlataforma, empresa = tdados_plataformas

        master.update({
                            idJogador: {"nickname": nickname, "jogo": nomeJogo, "rank": rank, "estudio": nomeStudio, "plataforma": nomePlataforma}
                        })
    return master

# ------------------------------------------------------------------------------
# 2.2) JUNÇÃO SELETIVA (TRIPLE JOIN)
# ------------------------------------------------------------------------------
def join_player_jogo_estudio(jogadores, jogos, estudios):
    """
    OBJETIVO: Juntar pelo menos 3 dicionários em uma estrutura simplificada.
    
    RECEBE:
        jogadores (dict): dicionário com ID do jogador → (ID jogo, rank)
        jogos     (dict): dicionário com ID jogo → (nome, ID estúdio)
        estudios  (dict): dicionário com ID estúdio → (nome, ID plataforma)
    
    RETORNA:
        list: Lista de tuplas no formato [(Player_ID, Jogo_Nome, Estudio_Nome), ...]
    
    DICA: Use .get() para acessar valores com segurança
    """
    lista = []
    for (idJogador, tIdJogoRank) in jogadores.items():
        idJogo, rank = tIdJogoRank

        tdados_jogos = jogos.get(idJogo)
        if tdados_jogos is None:
            continue
        nomeJogo, idEstudio = tdados_jogos

        tdados_estudios = estudios.get(idEstudio)
        if tdados_estudios is None:
            continue
        nomeEstudio, idPlataforma = tdados_estudios

        lista.append((idJogador,nomeJogo,nomeEstudio))

    return lista
# ------------------------------------------------------------------------------
# 2.3) INVERSÃO DE DICIONÁRIO (JOGADORES POR JOGO)
# ------------------------------------------------------------------------------
def inverter_jogadores_por_jogo(jogadores):
    """
    OBJETIVO: Descobrir quem joga o quê (Inverter Chave <-> Valor).
    
    RECEBE:
        jogadores (dict): dicionário {id_player: (id_jogo, rank)}
    
    RETORNA:
        dict: Dicionário {id_jogo: [lista_de_ids_dos_players]}
    
    DICA: Use setdefault() para criar listas automaticamente
    """
    novo_dict={}

    for id_player, tIdJogoRank in jogadores.items():
        if tIdJogoRank is None:
            continue
        idJogo, rank = tIdJogoRank

        novo_dict.setdefault(idJogo, []).append(id_player)
    

    return novo_dict

# ------------------------------------------------------------------------------
# 2.4) INVERSÃO DE DICIONÁRIO (JOGADORES POR RANK)
# ------------------------------------------------------------------------------
def inverter_jogadores_por_rank(jogadores):
    """
    OBJETIVO: Descobrir quais jogadores têm cada rank.
    
    RECEBE:
        jogadores (dict): dicionário {id_player: (id_jogo, rank)}
    
    RETORNA:
        dict: Dicionário {rank: [lista_de_ids_dos_players]}
    
    DICA: Use setdefault() para criar listas automaticamente
    """
    novo_dict={}

    for idPlayer, tIdJogoRank in jogadores.items():
        if tIdJogoRank is None:
            continue
        idJogo, rank = tIdJogoRank

        novo_dict.setdefault(rank, []).append(idPlayer)
        
    return novo_dict


# ------------------------------------------------------------------------------
# 2.5) FREQUÊNCIA DE ESTÚDIOS
# ------------------------------------------------------------------------------
def calcular_frequencia_estudios(master_dict):
    """
    OBJETIVO: Calcular quantos jogadores estão associados a cada estúdio.
    
    RECEBE:
        master_dict (dict): Dicionário Master criado na função 2.1
    
    RETORNA:
        dict: Dicionário {nome_estudio: quantidade_de_jogadores}
    
    DICA: Use .get() para contar
    """
    # idJogador: {"nickname": nickname, "jogo": nomeJogo, "rank": rank, "estudio": nomeStudio, "plataforma": nomePlataforma}

    #USANDO SETDEFAUL
    # frequencia = {}
    # for (jogador,dado) in master_dict.items():
    #     estudio = dado.get("estudio", "?")
    #     frequencia.setdefault(estudio, 0)
    #     frequencia[estudio]+=1
    # return frequencia

    frequencia = {}
    for (jogador,dado) in master_dict.items():
        estudio = dado.get("estudio")
        print(estudio)

        frequencia[estudio] = frequencia.get(estudio, 0) + 1
    return frequencia


# ------------------------------------------------------------------------------
# 2.6) AGRUPAMENTO POR PLATAFORMA
# ------------------------------------------------------------------------------
def agrupar_por_plataforma(master_dict):
    """
    OBJETIVO: Agrupar os nicknames dos jogadores por plataforma.
    
    RECEBE:
        master_dict (dict): Dicionário Master criado na função 2.1
    
    RETORNA:
        dict: Dicionário {plataforma: [lista_de_nicknames]}
    
    DICA: Use setdefault() para criar listas automaticamente
    """
    # idJogador: {"nickname": nickname, "jogo": nomeJogo, "rank": rank, "estudio": nomeStudio, "plataforma": nomePlataforma}


    novo_dict={}

    for (jogador,dado) in master_dict.items():
        plataforma = dado.get("plataforma")
        nickname = dado.get("nickname")

        novo_dict.setdefault(plataforma, []).append(nickname)
        
    return novo_dict
    pass


# ------------------------------------------------------------------------------
# 2.7) RELATÓRIO COMPLETO (FREQUÊNCIA + AGRUPAMENTO)
# ------------------------------------------------------------------------------
def relatorio_estatistico(master_dict):
    """
    OBJETIVO: Gerar frequência de estúdios e agrupamento por plataforma.
    
    RECEBE:
        master_dict (dict): Dicionário Master criado na função 2.1
    
    RETORNA:
        tuple: (dict_frequencia, dict_agrupamento)
    """
    # idJogador: {"nickname": nickname, "jogo": nomeJogo, "rank": rank, "estudio": nomeStudio, "plataforma": nomePlataforma}

    dict_frequencia = {}
    dict_agrupamento = {}

    for jogador, dados in master_dict.items():
        estudio = dados.get("estudio") or "?"
        plataforma = dados.get("plataforma") or "?"
        nickname = dados.get("nickname") or "?"

        dict_frequencia[estudio] = dict_frequencia.get(estudio, 0) + 1
        dict_agrupamento.setdefault(plataforma, []).append(nickname)

    return (dict_frequencia, dict_agrupamento)


# ------------------------------------------------------------------------------
# 2.8) DESAFIO: ENCONTRAR O JOGADOR COM MELHOR RANK
# ------------------------------------------------------------------------------
def rank_para_numero(rank):
    """
    OBJETIVO: Converter rank em número para comparação.
    
    RECEBE:
        rank (str): Nome do rank (ex: "Radiante", "Imortal", etc.)
    
    RETORNA:
        int: Valor numérico do rank (maior = melhor)
    
    DICA: Use um dicionário para mapear rank → valor
    """
    # COMPLETAR: Mapear cada rank para um valor numérico
    ordem = {
        'Radiante': 6,
        'Imortal': 5,
        'Global': 4,
        'Diamante': 3,
        'Elite': 2,
        'Ouro': 1
    }

    return ordem.get(rank, 0)

def encontrar_melhor_rank(master_dict):
    """
    OBJETIVO: Encontrar o jogador com o rank mais alto.
    
    RECEBE:
        master_dict (dict): Dicionário Master
    
    RETORNA:
        dict: Dicionário do jogador com melhor rank (ou None se vazio)
    
    DICA: Use a função rank_para_numero() para comparar
    """
    melhor_jogador = None
    melhor_valor = -1

    for jogador, dados in master_dict.items():
        rank = dados.get("rank")
        valor_rank = rank_para_numero(rank)

        if valor_rank > melhor_valor:
            melhor_valor = valor_rank
            melhor_jogador = dados

    return melhor_jogador


# ==============================================================================
# PARTE 3: TESTES (JÁ FORNECIDOS - NÃO ALTERAR)
# ==============================================================================

# Dicionário: ID do Jogador → (ID do Jogo, Rank)
d_jogadores = {
    10: ('LOL', 'Diamante'),
    20: ('VAL', 'Imortal'),
    30: ('LOL', 'Ouro'),
    40: ('FIFA', 'Elite'),
    50: ('VAL', 'Radiante'),
    60: ('CS2', 'Global')
}

# Dicionário: ID do Jogo → (Nome do Jogo, ID do Estúdio)
d_jogos = {
    'LOL': ('League of Legends', 'RIOT'),
    'VAL': ('Valorant', 'RIOT'),
    'CS2': ('Counter-Strike 2', 'VALVE')
}

# Dicionário: ID do Estúdio → (Nome do Estúdio, ID da Plataforma)
d_estudios = {
    'RIOT': ('Riot Games', 'PC'),
    'VALVE': ('Valve Corp', 'STEAM')
}

# Dicionário: ID da Plataforma → (Nome da Plataforma, Empresa)
d_plataformas = {
    'PC': ('Computador', 'Diversos'),
    'STEAM': ('Steam Deck', 'Valve')
}

# Dicionário: ID do Jogador → Nickname
d_nomes = {
    10: "Shadow",
    20: "Viper",
    30: "Pingu",
    40: "Goleiro",
    50: "Ace",
    60: "Sniper"
}
# print("=" * 70)
# print("SISTEMA DE ANÁLISE GAMER 2026 - TESTES")
# print("=" * 70)

# # --------------------------------------------------------------------------
# # TESTE 2.1: Criar Master Dict
# # --------------------------------------------------------------------------
print("\n[TESTE 2.1] Criando Dicionário Master...")
master = criar_master_dict(d_jogadores, d_jogos, d_estudios, d_plataformas, d_nomes)
print(master)
print("   Player 10:")
print(f"     Esperado: {{'nickname': 'Shadow', 'jogo': 'League of Legends', 'rank': 'Diamante', 'estudio': 'Riot Games', 'plataforma': 'Computador'}}")
print(f"     Obtido:   {master.get(10)}")

print("\n   Player 60:")
print(f"     Esperado: {{'nickname': 'Sniper', 'jogo': 'Counter-Strike 2', 'rank': 'Global', 'estudio': 'Valve Corp', 'plataforma': 'Steam Deck'}}")
print(f"     Obtido:   {master.get(60)}")

print(f"     Obtido:   {master.get(40)}")

# # --------------------------------------------------------------------------
# # TESTE 2.2: Triple Join
# # --------------------------------------------------------------------------
print("\n[TESTE 2.2] Triple Join (Player, Jogo, Estúdio)...")
triplo = join_player_jogo_estudio(d_jogadores, d_jogos, d_estudios)
print(f"   Primeiro resultado: {triplo[0] if triplo else 'Lista vazia'}")
print(f"   Esperado: (10, 'League of Legends', 'Riot Games')")

# # --------------------------------------------------------------------------
# # TESTE 2.3: Inversão por Jogo
# # --------------------------------------------------------------------------
print("\n[TESTE 2.3] Inversão: Jogadores por Jogo...")
jogo_invertido = inverter_jogadores_por_jogo(d_jogadores)
print(f"   Jogadores que jogam 'LOL': {jogo_invertido.get('LOL', [])}")
print(f"   Esperado: [10, 30]")

# # --------------------------------------------------------------------------
# # TESTE 2.4: Inversão por Rank
# # --------------------------------------------------------------------------
print("\n[TESTE 2.4] Inversão: Jogadores por Rank...")
rank_invertido = inverter_jogadores_por_rank(d_jogadores)
print(f"   Jogadores rank 'Diamante': {rank_invertido.get('Diamante', [])}")
print(f"   Esperado: [10]")

# # --------------------------------------------------------------------------
# # TESTE 2.5: Frequência de Estúdios
# # --------------------------------------------------------------------------
print("\n[TESTE 2.5] Frequência de Estúdios...")
freq_est = calcular_frequencia_estudios(master)
print(f"   Resultado: {freq_est}")
print(f"   Esperado: {{'Riot Games': 4, 'Valve Corp': 1, '?': 1}}")

# # --------------------------------------------------------------------------
# # TESTE 2.6: Agrupamento por Plataforma
# # --------------------------------------------------------------------------
print("\n[TESTE 2.6] Agrupamento por Plataforma...")
agrup_plat = agrupar_por_plataforma(master)
print(f"   Plataforma 'Computador': {agrup_plat.get('Computador', [])}")
print(f"   Esperado: ['Shadow', 'Viper', 'Pingu', 'Ace']")

# # --------------------------------------------------------------------------
# # TESTE 2.7: Relatório Estatístico
# # --------------------------------------------------------------------------
# print("\n[TESTE 2.7] Relatório Estatístico...")
# freq, agrup = relatorio_estatistico(master)
# print(f"   Frequência: {freq}")
# print(f"   Agrupamento: {agrup}")

# # --------------------------------------------------------------------------
# # TESTE 2.8: Melhor Rank
# # --------------------------------------------------------------------------
# print("\n[TESTE 2.8] Melhor Rank...")
# melhor = encontrar_melhor_rank(master)
# if melhor:
#     print(f"   Melhor jogador: {melhor['nickname']} - Rank: {melhor['rank']} - Jogo: {melhor['jogo']}")
#     print(f"   Esperado: Ace - Rank: Radiante - Jogo: Valorant")
    