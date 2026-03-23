# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 11:06:41 2026

@author: ferlin
"""
dCapitais = {
    "Brasil": "Brasília",
    "França": "Paris",
    "Japão": "Tóquio"
}
novo1={}   # chave: capital e o valor: país
for (pais,capital)    in dCapitais.items():
    novo1[capital] = pais

dAlunosTurma = {
    "Ana": "Turma A",
    "Bruno": "Turma B",
    "Carla": "Turma A",
    "Diego": "Turma B"
}

novo2={}   # chave: turma e o valor: alunos da turma
for (aluno,turma)    in dAlunosTurma.items():
    lAlunosAtual=novo2.get(turma,[])
    lAlunosAtual.append(aluno)
    novo2[turma]=lAlunosAtual

novo2={}   # chave: turma e o valor: alunos da turma
for (aluno,turma)    in dAlunosTurma.items():
    if turma not in novo2:
        novo2[turma]=[]
    novo2[turma].append(aluno)
############################################################

    
matr_login = {
    "202301": "ana.silva",
    "202302": "bruno.souza",
    "202303": "carla.melo"
}

login_senha = {
    "ana.silva": "1234",
    "bruno.souza": "abcd",
    "carla.melo": "xyz"
}
#juntando com o valor representado por um tupla
novo3={}
for (matr,login) in matr_login.items():
    senha=login_senha.get(login,"sem senha")   
    novo3[matr]= (login,senha)
    
print(novo3["202303"][1])


#juntando com o valor representado por um dicionário
novo4={}
for (matr,login) in matr_login.items():
    senha=login_senha.get(login,"sem senha")   
    novo4[matr]= {'login':login,'senha':senha}
    
print(novo4["202303"]['senha'])

novo5={}
for (matr,login) in matr_login.items():
    senha=login_senha.get(login,"sem senha")   
    novo5[matr]= {login:senha}
    
