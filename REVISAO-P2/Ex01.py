# -*- coding: utf-8 -*-
"""
EXERCÍCIOS EXTRAS DE REVISÃO P2 — PANDAS
VIGILÂNCIA EM SAÚDE PÚBLICA — UNIDADES BÁSICAS DE SAÚDE (UBS)
-------------------------------------------------------------------------------

12 EXERCÍCIOS GRADUADOS:
    4 × Nível MÉDIO        (M1 a M4)
    4 × Nível DIFÍCIL      (D1 a D4)
    4 × Nível MUITO DIFÍCIL (VD1 a VD4)

ATENÇÃO:
    Execute na MESMA pasta que contém: dados_ubs_vigilancia_saude.xlsx
    Todos os exercícios são independentes, mas use sempre os DataFrames
    carregados no bloco CARREGANDO DADOS (não recarregue dentro de cada questão).

IMPORTANTE:
    As conclusões são baseadas nos dados da amostra e não afirmam causalidade.
    Use expressões como:
        "na amostra"; "os dados sugerem"; "aparece associado";
        "merece atenção"; "não permite afirmar relação de causa e efeito".
"""

################################################################################
# Nome completo: Maria Luiza Lima Bastos
# Matrícula: 2320468
# Declaração de autoria: Sim
################################################################################

import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', '{:.2f}'.format)


# =============================================================================
# CARREGANDO DADOS
# =============================================================================

ARQUIVO = 'REVISAO-P2/dados_ubs_vigilancia_saude.xlsx'

dfUnidade     = pd.read_excel(ARQUIVO, sheet_name='unidade',     index_col=0)
dfAtendimento = pd.read_excel(ARQUIVO, sheet_name='atendimento', index_col=0)
dfGestao      = pd.read_excel(ARQUIVO, sheet_name='gestao',      index_col=0)

print('\n==============================================')
print('Exercícios Extras — Revisão P2 — Pandas / UBS')
print('==============================================\n')

print('Amostra inicial - dfUnidade:')
print(dfUnidade.head(3))
print('\nAmostra inicial - dfAtendimento:')
print(dfAtendimento.head(3))
print('\nAmostra inicial - dfGestao:')
print(dfGestao.head(3))


# =============================================================================
#  ██████████   NÍVEL MÉDIO   ██████████
# =============================================================================

# =============================================================================
# EXERCÍCIO M1 — Série, describe() e filtro por valor
# =============================================================================

print('\n==============================================')
print('M1 — Série, describe() e filtro por valor')
print('==============================================')

# -----------------------------------------------------------------------------
# M1.a) Extraia a coluna consultas_medicas de dfAtendimento como uma SÉRIE
#        e armazene em s_consultas.
#        Mostre as estatísticas descritivas completas de s_consultas.
#        Mostre separadamente: média, mediana e desvio padrão (três prints).
# -----------------------------------------------------------------------------

print('\nM1.a — Série de consultas_medicas: describe, média, mediana e desvio padrão')
# SEU CÓDIGO AQUI
s_consultas = dfAtendimento['consultas_medicas']

print(s_consultas.describe()) # como é uma series de valores quantitativos, o descrive retorna estatisticas numericas

print(s_consultas.mean())
print(s_consultas.median())
print(s_consultas.mode())

print(s_consultas.std())


# -----------------------------------------------------------------------------
# M1.b) Usando s_consultas, mostre os CINCO maiores valores da série
#        (sem mostrar o índice — use .values ou .tolist() após o sort).
#
#        Em seguida, mostre quantas UBS possuem consultas_medicas
#        ACIMA DA MÉDIA da própria série (use comparação booleana e .sum()).
# # -----------------------------------------------------------------------------

print('\nM1.b — Top-5 valores e contagem acima da média')
# # SEU CÓDIGO AQUI
s_ordena = s_consultas.sort_values()
print(s_ordena.head(5))

s_acima = s_consultas.loc[s_consultas>s_consultas.mean()]
print(s_acima.count()) # nao faz sentido usar sum aqui, pois ele soma pelo valor. queremos saber QWUANTAS UBS estao presente, para isso fazemos count.


# # -----------------------------------------------------------------------------
# # M1.c) Filtre dfAtendimento mantendo apenas as UBS cujo valor de
# #        consultas_medicas está ACIMA DA MÉDIA.
# #        Armazene em dfAcimaDaMedia.
# #
# #        Mostre:
# #          - quantas UBS estão nesse subgrupo
# #          - a média de cobertura_pct desse subgrupo
# #          - a média de cobertura_pct do restante (abaixo ou igual à média)
# #
# #        Compare as duas médias em um único print explicativo.
# # -----------------------------------------------------------------------------

print('\nM1.c — Cobertura média: acima vs. abaixo da média de consultas')
# # SEU CÓDIGO AQUI
condicao = dfAtendimento['consultas_medicas']>dfAtendimento['consultas_medicas'].mean()

dfAcimaDaMedia = dfAtendimento[condicao]
dfAbaixoDaMedia = dfAtendimento[~condicao]

qtd = dfAcimaDaMedia.count()
media_cobertura_pct = dfAcimaDaMedia['cobertura_pct'].mean()
media_cobertura_pct_rest = dfAbaixoDaMedia['cobertura_pct'].mean()

print(media_cobertura_pct, media_cobertura_pct_rest)


# # =============================================================================
# # EXERCÍCIO M2 — value_counts(), unique() e nunique() por grupo
# # =============================================================================

print('\n==============================================')
print('M2 — Frequências, valores únicos e contagens por grupo')
print('==============================================')

# # -----------------------------------------------------------------------------
# # M2.a) Em dfUnidade, mostre a tabela de frequência da coluna porte,
# #        com os percentuais (normalize=True), arredondados para 2 casas.
# #        Mostre também a tabela de frequência cruzada entre porte e informatizada
# #        usando pd.crosstab().
# # -----------------------------------------------------------------------------

print('\nM2.a — Frequência de porte e crosstab porte x informatizada')
# SEU CÓDIGO AQUI
print(dfUnidade.head(5))

# Para coluna de dados quantitativos
freq_absoluta = dfUnidade['porte'].value_counts() #fre absoluta (contagem)
freq_relativa = dfUnidade['porte'].value_counts(normalize=True)*100

tabela_freq_qualitativa = pd.DataFrame({
    'freq abs': freq_absoluta,
    'freq rel': freq_relativa,
})

tabela_freq_qualitativa['freq acum'] = tabela_freq_qualitativa['freq abs'].cumsum()

print(tabela_freq_qualitativa)

#para coluna de dados qualitativos
# idades = [22, 25, 19, 35, 40, 28, 55, 18, 60, 23]
# df_idades = pd.DataFrame({'Idade': idades})

# # Cria automaticamente 3 faixas/classes de idade e conta a frequência
# tabela_classes = df_idades['Idade'].value_counts(bins=3)
# print(tabela_classes)

# # -----------------------------------------------------------------------------
# # M2.b) Para cada REGIÃO de dfUnidade, mostre:
# #          - os municípios únicos (groupby + apply com unique)
# #          - quantos municípios distintos há (groupby + nunique)
# #
# #        Os dois resultados devem ser exibidos em prints separados e rotulados.
# # -----------------------------------------------------------------------------

print('\nM2.b — Municípios únicos e contagem por região')
# SEU CÓDIGO AQUI
unicos = dfUnidade.groupby('regiao')['municipio'].unique() #QUAIS sao distintos - Uma lista de valores.
nao_unicos = dfUnidade.groupby('regiao')['municipio'].nunique() #QUANTOS sao distintos - Um número inteiro.
print(nao_unicos)

# # -----------------------------------------------------------------------------
# # M2.c) Filtre dfUnidade mantendo apenas as UBS NÃO informatizadas.
# #        Armazene em dfNaoInfo.
# #        Mostre a modalidade mais frequente nesse subconjunto.
# #        Mostre também a tabela de frequência completa de modalidade
# #        nesse subconjunto.
# # -----------------------------------------------------------------------------

print('\nM2.c — Modalidade mais frequente entre UBS não informatizadas')
# SEU CÓDIGO AQUI
dfNaoInfo = dfUnidade[dfUnidade['informatizada']=='NÃO']
moda = dfNaoInfo.mode()

freq_absoluta = dfNaoInfo['modalidade'].value_counts() #fre absoluta (contagem)
freq_relativa = dfNaoInfo['modalidade'].value_counts(normalize=True)*100

tabela_freq_qualitativa = pd.DataFrame({
    'freq abs': freq_absoluta,
    'freq rel': freq_relativa,
})

tabela_freq_qualitativa['freq acum'] = tabela_freq_qualitativa['freq abs'].cumsum()


print(tabela_freq_qualitativa)
# # =============================================================================
# # EXERCÍCIO M3 — Criação de coluna booleana e filtros compostos
# # =============================================================================

print('\n==============================================')
print('M3 — Coluna booleana e filtros compostos')
print('==============================================')

# # -----------------------------------------------------------------------------
# # M3.a) Em dfGestao, crie a coluna risco_basico (True/False) que seja True
# #        quando PELO MENOS UMA das condições abaixo for verdadeira:
# #            superlotacao_pontual   == 'SIM'
# #            desabastecimento_critico == 'SIM'
# #
# #        Mostre a frequência absoluta de True e False em risco_basico.
# # -----------------------------------------------------------------------------

print('\nM3.a — Coluna risco_basico e sua frequência')
# SEU CÓDIGO AQUI
dfGestao['risco_basico'] = (dfGestao['superlotacao_pontual'] == 'SIM') | (dfGestao['desabastecimento_critico'] == 'SIM')

freq_absoluta = dfGestao['risco_basico'].value_counts()

print(freq_absoluta)

# # -----------------------------------------------------------------------------
# # M3.b) Entre as UBS com risco_basico == True, calcule:
# #            - a média de absenteismo_pct
# #            - a porcentagem que tem equipe_incompleta == 'SIM'
# #
# #        Compare com os mesmos valores do grupo risco_basico == False.
# #        Exiba os quatro resultados em um único DataFrame ou em prints claros.
# # -----------------------------------------------------------------------------

print('\nM3.b — Absenteísmo e equipe incompleta: risco básico vs. sem risco')
# SEU CÓDIGO AQUI

condicao = dfGestao['risco_basico']==True

df_risco_basico_true = dfGestao[condicao]
media_absenteismo = df_risco_basico_true['absenteismo_pct'].mean()
print(media_absenteismo)
equipe_incomp_count = df_risco_basico_true[df_risco_basico_true['equipe_incompleta']=='SIM'].nunique() #shape[0] pega a info de atd de linhas do df
percentual_equipe_incomp_count = equipe_incomp_count/(df_risco_basico_true.nunique())*100

print(percentual_equipe_incomp_count,'%')

df_risco_basico_false = dfGestao[~condicao]
media_absenteismo = df_risco_basico_false['absenteismo_pct'].mean()
print(media_absenteismo)
equipe_incomp_count = df_risco_basico_false[df_risco_basico_false['equipe_incompleta']=='SIM'].nunique() #shape[0] pega a info de atd de linhas do df
percentual_equipe_incomp_count = equipe_incomp_count/(df_risco_basico_false.nunique())*100

print(percentual_equipe_incomp_count,'%')


# # -----------------------------------------------------------------------------
# # M3.c) Crie um filtro composto que selecione UBS em que:
# #            equipe_incompleta       == 'SIM'   E
# #            prontuario_eletronico   == 'NÃO'   E
# #            abastecimento_regular   == 'NÃO'
# #
# #        Mostre quantas UBS atendem a essas três condições simultaneamente
# #        e liste o índice (ubs_id) dessas unidades.
# # -----------------------------------------------------------------------------

print('\nM3.c — UBS com tripla adversidade operacional')
# SEU CÓDIGO AQUI
df_filt_com = dfGestao[(dfGestao['equipe_incompleta']=='SIM') & (dfGestao['prontuario_eletronico']=='NÃO') & (dfGestao['abastecimento_regular']=='NÃO')]

df_qtd_atende = df_filt_com.nunique()
print(df_qtd_atende.shape[0]) #validar se essa é a melhor forma de fazer
print(df_qtd_atende.index)

# # =============================================================================
# # EXERCÍCIO M4 — Ordenação, slice e integração entre DataFrames
# # =============================================================================

print('\n==============================================')
print('M4 — Ordenação, slice e integração entre DataFrames')
print('==============================================')

# # -----------------------------------------------------------------------------
# # M4.a) Ordene dfAtendimento pela coluna cobertura_pct em ordem DECRESCENTE.
# #        Mostre as 10 primeiras linhas do resultado (top-10 cobertura).
# # -----------------------------------------------------------------------------

print('\nM4.a — Top-10 UBS por cobertura_pct')
# SEU CÓDIGO AQUI
df_ordenado_desc = dfAtendimento.sort_values(by='cobertura_pct',ascending=False)
print(df_ordenado_desc.head(10))


# # -----------------------------------------------------------------------------
# # M4.b) Usando pd.concat(axis=1), junte dfUnidade[['regiao', 'municipio', 'modalidade']]
# #        com dfAtendimento[['cobertura_pct', 'consultas_medicas']].
# #        Armazene em dfJunto.
# #
# #        Ordene dfJunto por cobertura_pct de forma decrescente e mostre
# #        as 10 primeiras linhas.
# # -----------------------------------------------------------------------------

print('\nM4.b — Integração e top-10 com informações de unidade')
# SEU CÓDIGO AQUI

dfJunto = pd.concat([dfUnidade[['regiao', 'municipio', 'modalidade']], dfAtendimento[['cobertura_pct', 'consultas_medicas']]] ,axis=1)

dfJunto_ord_desc = dfJunto.sort_values(by='cobertura_pct', ascending=False)
print(dfJunto_ord_desc.head(10))

# # -----------------------------------------------------------------------------
# # M4.c) Usando dfJunto, filtre apenas as UBS do município de 'Salvador'.
# #        Mostre a média de cobertura_pct e de consultas_medicas para Salvador.
# #        Em seguida, compare com a média geral de dfJunto.
# #        (dois prints: médias de Salvador e médias gerais)
# # -----------------------------------------------------------------------------

print('\nM4.c — Salvador vs. média geral: cobertura e consultas médicas')
# SEU CÓDIGO AQUI
dfJunto_fil_salvador = dfJunto[dfJunto['municipio']=='Salvador']

medias_cobertura_pct = dfJunto_fil_salvador['cobertura_pct'].mean()
medias_consultas_medicas = dfJunto_fil_salvador['consultas_medicas'].mean()

medias_dfJunto_cobertura_pct = dfJunto['cobertura_pct'].mean()
medias_dfJunto_consultas_medicas = dfJunto['consultas_medicas'].mean()

print("salvador ",medias_cobertura_pct, medias_consultas_medicas)
print("geral ",medias_dfJunto_cobertura_pct,medias_dfJunto_consultas_medicas)

# # =============================================================================
# #  ████████████   NÍVEL DIFÍCIL   ████████████
# # =============================================================================

# # =============================================================================
# # EXERCÍCIO D1 — groupby com múltiplas funções de agregação
# # =============================================================================

print('\n==============================================')
print('D1 — groupby com múltiplas funções de agregação')
print('==============================================')

# # -----------------------------------------------------------------------------
# # D1.a) Concatene dfUnidade e dfAtendimento (axis=1) em dfCompleto.
# #
# #        Faça um groupby por MODALIDADE E PORTE (lista de colunas) e calcule,
# #        em um único .agg() com dicionário:
# #            - média de consultas_medicas
# #            - média de cobertura_pct
# #            - soma de visitas_domiciliares
# #            - máximo de procedimentos_odonto
# #
# #        Ordene o resultado pela maior média de consultas_medicas (decrescente).
# # -----------------------------------------------------------------------------

# print('\nD1.a — Produção assistencial por modalidade e porte')

# # SEU CÓDIGO AQUI


# # -----------------------------------------------------------------------------
# # D1.b) Usando dfCompleto, agrupe apenas por REGIÃO e calcule:
# #            - tamanho de cada grupo (count de consultas_medicas)
# #            - média de consultas_medicas
# #            - média de cobertura_pct
# #            - mínimo e máximo de cobertura_pct
# #
# #        Tudo em um único .agg(). Exiba o resultado.
# # -----------------------------------------------------------------------------

# print('\nD1.b — Estatísticas de atendimento por região')

# # SEU CÓDIGO AQUI


# # -----------------------------------------------------------------------------
# # D1.c) Com dfCompleto, mostre — por MODALIDADE — quantas UBS possuem
# #        cobertura_pct acima de 50.
# #        Use groupby + apply com função lambda que filtra e conta.
# # -----------------------------------------------------------------------------

# print('\nD1.c — Quantas UBS com cobertura > 50% por modalidade')

# # SEU CÓDIGO AQUI


# # =============================================================================
# # EXERCÍCIO D2 — pd.cut com labels e análise cruzada
# # =============================================================================

# print('\n==============================================')
# print('D2 — pd.cut com labels e análise cruzada')
# print('==============================================')

# # -----------------------------------------------------------------------------
# # D2.a) Em dfGestao, crie a coluna FaixaAbsenteismo classificando
# #        absenteismo_pct em QUATRO faixas com os seguintes limites manuais:
# #            0 até  8  →  'Absenteísmo baixo'
# #            8 até 16  →  'Absenteísmo moderado'
# #           16 até 25  →  'Absenteísmo elevado'
# #           25 até 40  →  'Absenteísmo crítico'
# #
# #        Mostre a frequência absoluta de cada faixa.
# # -----------------------------------------------------------------------------

# print('\nD2.a — Coluna FaixaAbsenteismo com pd.cut')

# # SEU CÓDIGO AQUI


# # -----------------------------------------------------------------------------
# # D2.b) Faça um pd.crosstab entre FaixaAbsenteismo e prontuario_eletronico
# #        com totais de linha e coluna (margins=True, margins_name='Total').
# #
# #        Em seguida, faça outro crosstab com normalize='index' (frequência
# #        relativa por linha, em %) e arredonde para 2 casas decimais.
# #        Multiplique por 100 para exibir em percentual.
# # -----------------------------------------------------------------------------

# print('\nD2.b — Crosstab FaixaAbsenteismo x prontuario_eletronico (absoluto e %)')

# # SEU CÓDIGO AQUI


# # -----------------------------------------------------------------------------
# # D2.c) Mostre a média de absenteismo_pct agrupada por:
# #            abastecimento_regular E equipe_incompleta
# #        Ordene da maior para a menor média.
# #        Interprete em um print qual combinação apresenta o maior absenteísmo médio.
# # -----------------------------------------------------------------------------

# print('\nD2.c — Absenteísmo médio: abastecimento regular x equipe incompleta')

# # SEU CÓDIGO AQUI


# # =============================================================================
# # EXERCÍCIO D3 — Filtro por índice com .str e análise de subgrupo
# # =============================================================================

# print('\n==============================================')
# print('D3 — Filtro por índice com .str e análise de subgrupo')
# print('==============================================')

# # -----------------------------------------------------------------------------
# # D3.a) Em dfUnidade, use o ÍNDICE (ubs_id) para filtrar as UBS da
# #        macro-região Centro-Oeste (índice começa com 'CO').
# #        Use o método .str.startswith() sobre dfUnidade.index.
# #        Armazene em dfCO.
# #
# #        Mostre:
# #          - quantas UBS estão em dfCO
# #          - a frequência de porte em dfCO
# #          - a frequência de modalidade em dfCO
# # -----------------------------------------------------------------------------

# print('\nD3.a — Subgrupo Centro-Oeste: porte e modalidade')

# # SEU CÓDIGO AQUI


# # -----------------------------------------------------------------------------
# # D3.b) Usando dfAtendimento.loc[dfCO.index], calcule as médias de todas
# #        as colunas numéricas para as UBS do Centro-Oeste.
# #
# #        Compare com as médias gerais de dfAtendimento (mesmo .mean()).
# #        Mostre a diferença absoluta entre as duas médias (CO - geral).
# # -----------------------------------------------------------------------------

# print('\nD3.b — Médias de atendimento no Centro-Oeste vs. média geral')

# # SEU CÓDIGO AQUI


# # -----------------------------------------------------------------------------
# # D3.c) Use str.contains() com regex para filtrar UBS cujo índice
# #        contenha 'NE' OU 'SL' (Nordeste ou Sul).
# #        Armazene em dfNE_SL.
# #
# #        Nesse subgrupo, mostre:
# #          - a modalidade mais frequente (mode())
# #          - a UBS com MAIOR cobertura_pct (usando dfAtendimento.loc[...])
# # -----------------------------------------------------------------------------

# print('\nD3.c — Nordeste e Sul: modalidade predominante e UBS com maior cobertura')

# # SEU CÓDIGO AQUI


# # =============================================================================
# # EXERCÍCIO D4 — apply, map e isin
# # =============================================================================

# print('\n==============================================')
# print('D4 — apply, map e isin')
# print('==============================================')

# # -----------------------------------------------------------------------------
# # D4.a) Crie a função classifica_porte que receba um valor de porte e retorne:
# #            'Pequeno'  →  'Estrutura Pequena'
# #            'Médio'    →  'Estrutura Média'
# #            'Grande'   →  'Estrutura Ampliada'
# #
# #        Aplique em dfUnidade['porte'] usando .map() e armazene em
# #        dfUnidade['porte_descritivo'].
# #        Mostre a frequência da nova coluna.
# # -----------------------------------------------------------------------------

# print('\nD4.a — Coluna porte_descritivo com map')

# # SEU CÓDIGO AQUI


# # -----------------------------------------------------------------------------
# # D4.b) Em dfUnidade, use .isin() para filtrar apenas as UBS dos municípios:
# #            ['Fortaleza', 'Salvador', 'Recife', 'Natal']  (capitais nordestinas)
# #        Armazene em dfNordesteCap.
# #
# #        Usando dfAtendimento.loc[dfNordesteCap.index], calcule:
# #            - média de consultas_medicas por município
# #            - média de cobertura_pct por município
# #        (use pd.concat e groupby)
# # -----------------------------------------------------------------------------

# print('\nD4.b — Capitais nordestinas: consultas e cobertura por município')

# # SEU CÓDIGO AQUI


# # -----------------------------------------------------------------------------
# # D4.c) Usando dfAtendimento, crie com .apply(axis=1) a coluna
# #        produtividade_total como:
# #            consultas_medicas + consultas_enfermagem + visitas_domiciliares
# #
# #        Em seguida, crie a coluna categoria_produtividade usando .apply()
# #        com uma função que receba a linha inteira e retorne:
# #            'Alta'   se produtividade_total  > 700
# #            'Média'  se produtividade_total  entre 400 e 700 (inclusive)
# #            'Baixa'  se produtividade_total  < 400
# #
# #        Mostre a frequência de categoria_produtividade.
# # -----------------------------------------------------------------------------

# print('\nD4.c — Coluna produtividade_total e categoria_produtividade com apply')

# # SEU CÓDIGO AQUI


# # =============================================================================
# #  ████████████████   NÍVEL MUITO DIFÍCIL   ████████████████
# # =============================================================================

# # =============================================================================
# # EXERCÍCIO VD1 — groupby + transform + filtros condicionais encadeados
# # =============================================================================

# print('\n==============================================')
# print('VD1 — transform, medianas por grupo e filtros encadeados')
# print('==============================================')

# # -----------------------------------------------------------------------------
# # VD1.a) Concatene dfUnidade['modalidade'] com dfAtendimento em dfAux.
# #
# #         Usando groupby('modalidade') + transform('median'),
# #         crie em dfAux a coluna mediana_cobertura_por_modalidade
# #         (a mediana de cobertura_pct DENTRO de cada modalidade, expandida
# #         para cada linha — sem reduzir o DataFrame).
# #
# #         Crie em dfAux a coluna acima_mediana_modal (True/False):
# #             True  quando cobertura_pct > mediana_cobertura_por_modalidade
# #             False caso contrário
# #
# #         Mostre a frequência de True/False por modalidade usando
# #         groupby('modalidade')['acima_mediana_modal'].value_counts().
# # -----------------------------------------------------------------------------

# print('\nVD1.a — Mediana de cobertura por modalidade via transform e flag acima_mediana_modal')

# # SEU CÓDIGO AQUI


# # -----------------------------------------------------------------------------
# # VD1.b) Entre as UBS com acima_mediana_modal == True,
# #         filtre ainda as que têm equipe_incompleta == 'SIM'
# #         (use dfGestao.loc[...]).
# #
# #         Mostre quantas UBS atendem a esse critério duplo por MODALIDADE.
# #         Mostre também a média de absenteismo_pct dessas UBS por modalidade.
# # -----------------------------------------------------------------------------

# print('\nVD1.b — UBS acima da mediana modal E com equipe incompleta: contagem e absenteísmo')

# # SEU CÓDIGO AQUI


# # -----------------------------------------------------------------------------
# # VD1.c) Calcule — para cada REGIÃO (usando dfUnidade) — a porcentagem de
# #         UBS que estão ACIMA da mediana de consultas_medicas da própria região.
# #
# #         Use groupby + transform('median') sobre dfCompleto (região + atendimento).
# #         Resultado esperado: uma série com a % por região (de 0 a 100).
# # -----------------------------------------------------------------------------

# print('\nVD1.c — % de UBS acima da mediana regional de consultas médicas')

# # SEU CÓDIGO AQUI


# # =============================================================================
# # EXERCÍCIO VD2 — Score composto de vulnerabilidade e pivot_table
# # =============================================================================

# print('\n==============================================')
# print('VD2 — Score de vulnerabilidade e pivot_table')
# print('==============================================')

# # -----------------------------------------------------------------------------
# # VD2.a) Em dfGestao, crie a coluna score_vulnerabilidade somando pontos:
# #
# #             +1  se abastecimento_regular   == 'NÃO'
# #             +1  se equipe_incompleta       == 'SIM'
# #             +1  se superlotacao_pontual    == 'SIM'
# #             +1  se desabastecimento_critico== 'SIM'
# #             +1  se prontuario_eletronico   == 'NÃO'
# #             +2  se absenteismo_pct         >  20     (peso maior)
# #
# #         O score varia de 0 a 7.
# #         Mostre a frequência de cada valor de score_vulnerabilidade.
# # -----------------------------------------------------------------------------

# print('\nVD2.a — Score de vulnerabilidade operacional (0–7)')

# # SEU CÓDIGO AQUI


# # -----------------------------------------------------------------------------
# # VD2.b) Crie a coluna categoria_vulnerabilidade com base no score:
# #             0 a 1  →  'Baixa vulnerabilidade'
# #             2 a 3  →  'Vulnerabilidade moderada'
# #             4 a 5  →  'Alta vulnerabilidade'
# #             6 a 7  →  'Vulnerabilidade crítica'
# #         Use pd.cut com bins manuais.
# #
# #         Mostre a frequência absoluta de categoria_vulnerabilidade.
# #         Faça um gráfico de barras horizontais com essa frequência.
# # -----------------------------------------------------------------------------

# print('\nVD2.b — Categorias de vulnerabilidade e gráfico')

# # SEU CÓDIGO AQUI


# # -----------------------------------------------------------------------------
# # VD2.c) Construa uma pivot_table com:
# #             index   = categoria_vulnerabilidade
# #             columns = dfUnidade['modalidade']     (use pd.concat para unir)
# #             values  = score_vulnerabilidade
# #             aggfunc = 'mean'
# #
# #         Arredonde para 2 casas. Substitua NaN por '-'.
# #         Adicione os totais de linha usando .mean(axis=1) e
# #         os totais de coluna usando .mean(axis=0) e exiba tudo junto.
# # -----------------------------------------------------------------------------

# print('\nVD2.c — Pivot: score médio por categoria de vulnerabilidade x modalidade')

# # SEU CÓDIGO AQUI


# # =============================================================================
# # EXERCÍCIO VD3 — crosstab normalizado, comparação de subgrupos e ranking
# # =============================================================================

# print('\n==============================================')
# print('VD3 — crosstab normalizado, comparação de subgrupos e ranking')
# print('==============================================')

# # -----------------------------------------------------------------------------
# # VD3.a) Junte dfUnidade, dfAtendimento e dfGestao em dfTudo (pd.concat, axis=1).
# #
# #         Crie a coluna cobertura_alta (True/False):
# #             True  quando cobertura_pct >= 50
# #             False caso contrário
# #
# #         Faça um pd.crosstab entre regiao e cobertura_alta,
# #         normalizado por LINHA (normalize='index'), multiplicado por 100.
# #         Arredonde para 1 casa decimal.
# #         Interprete em um print qual região tem a maior proporção de UBS
# #         com cobertura alta.
# # -----------------------------------------------------------------------------

# print('\nVD3.a — Proporção de UBS com cobertura alta por região (%)')

# # SEU CÓDIGO AQUI


# # -----------------------------------------------------------------------------
# # VD3.b) Dentro de dfTudo, compare as UBS informatizadas (SIM) vs.
# #         não informatizadas (NÃO) calculando, por grupo:
# #             - média de absenteismo_pct
# #             - média de cobertura_pct
# #             - % com abastecimento_regular == 'SIM'
# #             - % com prontuario_eletronico == 'SIM'
# #
# #         Exiba os resultados em uma tabela com as duas colunas (SIM / NÃO)
# #         e quatro linhas (uma por métrica).
# # -----------------------------------------------------------------------------

# print('\nVD3.b — Informatizada vs. não informatizada: métricas comparativas')

# # SEU CÓDIGO AQUI


# # -----------------------------------------------------------------------------
# # VD3.c) Monte um RANKING das 10 UBS com PIOR desempenho combinado,
# #         definido pelo seguinte critério de ordenação multi-coluna:
# #
# #             1º critério: cobertura_pct          CRESCENTE  (menor é pior)
# #             2º critério: absenteismo_pct        DECRESCENTE (maior é pior)
# #             3º critério: score_vulnerabilidade  DECRESCENTE (maior é pior)
# #
# #         Mostre para cada UBS: regiao, porte, modalidade, municipio,
# #         cobertura_pct, absenteismo_pct e score_vulnerabilidade.
# #
# #         Dica: use dfTudo.sort_values() com listas de colunas e ascending=[].
# # -----------------------------------------------------------------------------

# print('\nVD3.c — Ranking das 10 UBS com pior desempenho combinado')

# # SEU CÓDIGO AQUI


# # =============================================================================
# # EXERCÍCIO VD4 — Pipeline analítico integrado
# # =============================================================================

# print('\n==============================================')
# print('VD4 — Pipeline analítico integrado')
# print('==============================================')

# # -----------------------------------------------------------------------------
# # VD4.a) Em dfGestao, padronize a coluna busca_ativa_faltosos
# #         seguindo as mesmas regras do template original (Q1.d):
# #
# #             Realiza / realiza / R / r / Sim / sim / SIM / S / s  →  'SIM'
# #             Não realiza / nao realiza / NR / nr / Não / nao /
# #             não / NÃO / N / n                                     →  'NÃO'
# #
# #         Armazene o resultado na própria coluna busca_ativa_faltosos.
# #         Mostre a frequência após a padronização.
# # -----------------------------------------------------------------------------

# print('\nVD4.a — Padronização de busca_ativa_faltosos')

# # SEU CÓDIGO AQUI


# # -----------------------------------------------------------------------------
# # VD4.b) A partir de dfTudo (construído em VD3.a), crie o dfAlerta
# #         filtrando as UBS que atendem a TODAS as condições abaixo:
# #
# #             cobertura_pct         < 20
# #             absenteismo_pct       > 15
# #             equipe_incompleta     == 'SIM'
# #             busca_ativa_faltosos  == 'NÃO'     (após padronização de VD4.a)
# #
# #         Mostre quantas UBS estão em dfAlerta.
# #         Mostre a distribuição dessas UBS por REGIÃO e por MODALIDADE
# #         (dois value_counts separados).
# # -----------------------------------------------------------------------------

# print('\nVD4.b — dfAlerta: UBS com quadrúpla condição crítica')

# # SEU CÓDIGO AQUI


# # -----------------------------------------------------------------------------
# # VD4.c) Para as UBS em dfAlerta, produza um RELATÓRIO SÍNTESE com:
# #
# #         1) Média de cobertura_pct e absenteismo_pct do grupo
# #         2) Modalidade mais frequente
# #         3) Região com maior número de UBS no grupo
# #         4) % de UBS informatizadas no grupo
# #         5) Média de score_vulnerabilidade do grupo
# #            (use dfGestao.loc[dfAlerta.index, 'score_vulnerabilidade'] —
# #             certifique-se de ter criado essa coluna em VD2.a antes)
# #
# #         Exiba cada item em um print rotulado.
# #         Ao final, escreva — em um comentário ou print — uma análise
# #         interpretativa de 3 a 5 linhas sobre o perfil das UBS em dfAlerta,
# #         usando as expressões de cautela indicadas no cabeçalho.
# # -----------------------------------------------------------------------------

# print('\nVD4.c — Relatório síntese do grupo de alerta')

# # SEU CÓDIGO AQUI


# # Análise interpretativa (3 a 5 linhas):
# # ESCREVA AQUI


# print('\n==============================================')
# print('Fim dos exercícios extras de revisão.')
# print('==============================================')