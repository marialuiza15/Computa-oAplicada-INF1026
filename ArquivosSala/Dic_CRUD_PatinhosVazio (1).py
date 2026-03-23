# -*- coding: utf-8 -*-
"""
Created on Sun Mar 14 15:30:27 2021

@author: Ferlin
"""
def calcIMC(alt,massa):
    return massa/(alt**2)

def obtemPatinho():
    nome=input("Nome?")
    alt=float(input("Altura de %s?"%nome))
    peso=float(input("Peso de %s?"%nome))
    return (nome, [alt,peso])

tPatinhos =  (('Huguinho',[1.20,45]),
              ('Luisinho',[1.10,60]),
              ('Zezinho',[1.00,100]),
              ('Patinhas',[1.10,40 ]),
              ('Clarabela', [2.3, 80]),
              ('Donald',[1.20,50]))
'''
1) Crie o dicionário de patinhos onde a chave é o nome e o valor a lista com alt, massa
    exiba-o
2) Sobre o dicionário de Patinhos:
  -->Recuperando valor de uma chave (acessando um item)
    a) Mostre os dados do Donald
    b) Mostre os dados de um patinho cujo nome é fornecido pelo usuário
        Se não existir??? --> exibir mensagem fulano não consta no dicionário
        Se não existir --> perguntar os dados e incluí-lo
        
  --> Inserindo/Alterando um item    
    c) Inclua o Peninha com 1.20m e 60 kg    
    d) Altere a altura do Donald para 1.30
    e) Obtenha o nome, altura e massa de um patinho via teclado
       Se o patinho já existe--> atualizar dados
       Se o patinho não existe --> incluir
       
  --> Visões e Percurso
    f) Mostre o nome dos patinhos no dicionário  
    g)	Acrescente ao peso dos 3 primeiros patinhos (considerando a ordem alfabética do nome), 10% do peso médio
        Dica: Classificar as chaves por nome
    h) Construa uma tupla com a altura e o peso médio dos patinhos (acessar só os valores)   
    i)	Iterando sobre o dicionário: Mostre o nome e o IMC (peso/altura2) de cada um
        •	Modificação: Construa um novo dicionário cuja chave é o nome e o valor é o IMC
        
  --> Atualizando vários elementos de um dicionário com update
    j)	Atualize o dicionário  dPat com o seguinte dicionário:
        d2= {'Clarabela': [2.20,78],'Margarida':[1.10,40]  }
        
  --> Eliminando um item
    k) Retire o Peninha exibindo seus dados

'''