# -*- coding: utf-8 -*-
"""
Considere os seguintes dicionários:
• Dicionário cidade_para_estado: Este dicionário mapeia o nome de várias cidades para seus respectivos
estados. Cada entrada no dicionário tem o nome da cidade como chave e a sigla do estado como valor.
Por exemplo, a cidade "São Paulo" é mapeada para o estado "SP", e a cidade "Salvador" é mapeada para o
estado "BA".
• Dicionário estado_para_regiao: Este dicionário mapeia as siglas dos estados para as regiões geográficas do
Brasil. A chave é a sigla do estado (como "SP" para São Paulo), e o valor é o nome da região geográfica à qual
o estado pertence (como "Sudeste").
Por exemplo, o estado "SP" está associado à região "Sudeste", enquanto o estado "BA" está associado à região
"Nordeste".
Construa a função informar_regiao_por_cidade que recebe os dicionários e o nome de uma cidade e deve exibir aa
região geográfica onde essa cidade está localizada. Se a cidade ou o estado não forem encontrados nos dicionários, a
função exibe uma mensagem informando que a cidade ou a região não foi encontrada.

"""

def informar_regiao_por_cidade(cidade):
    estado = cidade_para_estado.get(cidade)
    if estado:
        regiao = estado_para_regiao.get(estado)
        if regiao:
            print(f"A cidade de {cidade} está na região {regiao}.")
        else:
            print(f"Região para o estado '{estado}' não encontrada.")
    else:
        print(f"Cidade '{cidade}' não encontrada.")


 
# Dicionário que mapeia cidades para seus respectivos estados
cidade_para_estado = {
    "São Paulo": "SP",
    "Rio de Janeiro": "RJ",
    "Belo Horizonte": "MG",
    "Salvador": "BA",
    "Curitiba": "PR",
    "Porto Alegre": "RS",
    "Recife": "PE",
    "Manaus": "AM",
    "Florianópolis":"SC"
}

# Dicionário que mapeia estados para suas respectivas regiões
estado_para_regiao = {
    "SP": "Sudeste",
    "RJ": "Sudeste",
    "MG": "Sudeste",
    "BA": "Nordeste",
    "PR": "Sul",
    "RS": "Sul",
    "PE": "Nordeste",
    "AM": "Norte"
}


# Teste: Informar a região para algumas cidades
informar_regiao_por_cidade("Rio de Janeiro")
informar_regiao_por_cidade("Florianópolis")
informar_regiao_por_cidade("Campo Grande")