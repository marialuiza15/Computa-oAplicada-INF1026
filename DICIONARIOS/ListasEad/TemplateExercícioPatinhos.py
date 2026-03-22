
'''
A) Crie o dicionário de patinhos onde a chave é o nome e o valor a lista com alt, massa
    exiba-o
    
'''

dicionario={'Donald': [24, 12]}

'''
B) Sobre o dicionário de Patinhos:
  -->Recuperando valor de uma chave (acessando um item)
    a) Mostre os dados do Donald
    b) Mostre os dados de um patinho cujo nome é fornecido pelo usuário
        Se não existir??? --> exibir mensagem fulano não consta no dicionário
        Se não existir --> perguntar os dados e incluí-lo
'''
print(f"Exibindo dados do patinho Donald: {dicionario['Donald'][0]}, {dicionario['Donald'][1]}",)
'''
        
  --> Inserindo/Alterando um item    
    c) Inclua o Peninha com 1.20m e 60 kg    
    d) Altere a altura do Donald para 1.30
    e) Obtenha o nome, altura e massa de um patinho via teclado
       Se o patinho já existe--> atualizar dados
       Se o patinho não existe --> incluir
'''
dicionario.update({'Peninha': [120, 60]})
dicionario.update({'Donald': [130,12]})


nome=input("Insira o nome do patinho: ")
alt=int(input("Insira a altura do patinho: "))
massa=int(input("Insira a massa do patinho: "))


if nome in dicionario.keys():
    dicionario[nome][0]=alt
    dicionario[nome][1]=massa
else:
    dicionario.update({nome: [alt,massa]})

'''
       
  --> Visões e Percurso
    f) Mostre o nome dos patinhos no dicionário  
    g)	Acrescente ao peso dos 3 primeiros patinhos (considerando a ordem alfabética do nome), 10% do peso médio
        Dica: Classificar as chaves por nome
    h) Construa uma tupla com a altura e o peso médio dos patinhos (acessar só os valores)   
    i)	Iterando sobre o dicionário: Mostre o nome e o IMC (peso/altura2) de cada um
        •	Modificação: Construa um novo dicionário cuja chave é o nome e o valor é o IMC
'''

print(f"Nomes dos patinhos: {list(dicionario.keys())}")

dicionario_ordenado = dict(sorted(dicionario.items()))

pesomedio=0
# Exibindo os patinhos ordenados
for indice, nome_pato in enumerate(dicionario.keys()):
    if indice<3:
        pesomedio += dicionario[nome_pato][1]
        print(f"Peso do patinho {nome_pato} antes: {dicionario[nome_pato][1]}")

partepesomedio = 0.1*(pesomedio/3)

for indice, nome_pato in enumerate(dicionario.keys()):
    if indice<3:
        dicionario_ordenado[nome_pato][1]+=partepesomedio
        print(f"Peso do patinho {nome_pato} depois: {dicionario[nome_pato][1]}")

altmedia = 0
pesmedio = 0
lista = []
for pato in dicionario.keys():
    altmedia+=dicionario_ordenado[pato][0]
    pesmedio+=dicionario_ordenado[pato][1]

print((altmedia/len(dicionario_ordenado), pesmedio/len(dicionario_ordenado)))

def calcIMC(alt,massa):
    return massa/(alt**2)

dicionario_imc = {}

for pato in dicionario_ordenado.keys():
    dicionario_imc[pato] = calcIMC(dicionario_ordenado[pato][0],dicionario_ordenado[pato][1])
    
print(dicionario_imc.items())

'''
  --> Atualizando vários elementos de um dicionário com update
    j)	Atualize o dicionário  dPat com o seguinte dicionário:
        d2= {'Clarabela': [2.20,78],'Margarida':[1.10,40]  }
        
  --> Eliminando um item
    k) Retire o Peninha exibindo seus dados

'''
dPat = dicionario_ordenado.copy()

dPat.update({
    'Clarabela': [2.20,78],
    'Margarida':[1.10,40] 
})

print(dPat.keys())

removido = dPat.pop('Peninha')
print(f"Peninha removido. Dados: {removido}")
