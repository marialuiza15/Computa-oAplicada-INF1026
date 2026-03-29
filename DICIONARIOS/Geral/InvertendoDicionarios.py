# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:18:18 2020

@author: lcam
"""
'''
Construcao de dicionario inverso:
    - recebe dicionario com pessoa: lista das cores favoritas
    - retorna dicionario com COR: lista das pessoas que gostam dessa cor
Obs: uma pessoa pode ter várias cores preferidas
'''


dicPessoaECores={  'LALA': ['ROSA','AMARELO'],
                   'MIMI': ['ROSA','PRETO'],
                   'GUGU': ['VERDE','AZUL','BRANCO'],
                   'LELE': ['VERMELHO'],
                   'LILI': ['ROSA','AZUL'],
                   'VAVA': ['AMARELO','ROXO'],
                   'DEDE': ['AMARELO','VERDE','AZUL']}
    

def criaDicPorCor (dPorPessoa):
    dicPorCor = {}
    for (pessoa, lcores) in dPorPessoa.items():
        #aqui tem que tratar cada cor da lista de cores da pessoa
        for cor in lcores:
            #recuperar a lista de pessoas dessa cor no dic em construcao dicPorCor
            lPessoasDaCor = dicPorCor.get(cor,[])
            lPessoasDaCor.append(pessoa)
            dicPorCor[cor]=lPessoasDaCor                    
    return dicPorCor

print("\nDicionario com cor e lista das pessoas que preferem a cor")
dCores= criaDicPorCor(dicPessoaECores)
print(dCores)



'''
Dicionario de dicionario
            Dicionario de pets em que cada elemento eh:
            NomeDoPet : {dicionario interno com caracteristicas do pet}

'''
dMeusPets= { 'SONECA': {'tipo': 'gato', 'idade':8, 'sexo':'macho'},
             'PITUCO': {'tipo': 'cachorro', 'idade':7, 'sexo':'macho'},
             'DUKESA': {'tipo': 'gato', 'idade':4, 'sexo':'femea'},
             'SAPECA': {'tipo': 'cachorro', 'idade':2, 'sexo':'macho'},
             'LILIKA': {'tipo': 'cachorro', 'idade':2, 'sexo':'femea'},
             'FOFOCA': {'tipo': 'kalopsita','idade':6, 'sexo':'macho'}}


# RESPONDA:
print("\nDicionario PETs e suas caracteristicas")
print(dMeusPets)
# Quais as caracteristicas da DUKESA?
print("\nQuais as caracteristicas da DUKESA?")
print(dMeusPets['DUKESA'])
# Qual o tipo do PITUCO?
print("\nQual o tipo do PITUCO?")
print(dMeusPets['PITUCO']['tipo'])
# Qual a idade da LILIKA?
print("\nQual a idade da LILIKA?")
print(dMeusPets['LILIKA']['idade'])
# EXIBIR nome do pet e suas caracteristicas (para todos os pets)
print("\nPETs e suas caracteristicas")
for (pet, dcarac) in dMeusPets.items():
    print("\nPET:",pet)
    for (carac, valor) in dcarac.items(): #recupera elementos/itens do dic interno
        print('   ',carac,' = ',valor)

# EXIBIR o nome de todos os pets do tipo cachorro => CUIDADO: aqui acaba tendo uma busca
print("\nTodos os cachorros")
for (pet, dcarac) in dMeusPets.items():
    if dcarac['tipo'] == 'cachorro':
        print(pet)
        

"""
# INVERSO: caracteristica : {dicionario com animais e seus valores para a caracteristica}
"""
def criaDicPorCarac(dPorPet):
    dPorCarac = {}
    for (pet, dcarac) in dPorPet.items(): 
        for (carac, valor) in dcarac.items():
            dzinhoPetValorDaCarac = dPorCarac.get(carac, {})
            dzinhoPetValorDaCarac[pet]= valor
            dPorCarac[carac] = dzinhoPetValorDaCarac
    return dPorCarac

dicPorCarac = criaDicPorCarac(dMeusPets)
print(dicPorCarac)

