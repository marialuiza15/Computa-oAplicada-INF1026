#Contexto: Catálogo de Filmes 

# Dados iniciais: (título, [ano, duração, nota])
tFilmes = (('Matrix', [1999, 136, 9.0]),
           ('Titanic', [1997, 195, 8.5]),
           ('Avatar', [2009, 162, 8.0]),
           ('Star Wars', [1977, 121, 9.5]),
           ('O Rei Leão', [1994, 88, 9.0]),
           ('Interestelar', [2014, 169, 9.5]))

def calcNotaCategoria(nota):
    if nota >= 9:
        return "Excelente"
    elif nota >= 8:
        return "Muito Bom"
    elif nota >= 7:
        return "Bom"
    else:
        return "Regular"

def obterFilme():
    titulo = input("Título? ")
    ano = int(input("Ano de %s? " % titulo))
    duracao = int(input("Duração (minutos) de %s? " % titulo))
    nota = float(input("Nota (0-10) de %s? " % titulo))
    return (titulo, [ano, duracao, nota])

# A) Crie o dicionário dFilmes com os títulos, ano, duração e nota, a partir da tupla abaixo:
tFilmes = (('Matrix', [1999, 136, 9.0]),
           ('Titanic', [1997, 195, 8.5]),
           ('Avatar', [2009, 162, 8.0]),
           ('Star Wars', [1977, 121, 9.5]),
           ('O Rei Leão', [1994, 88, 9.0]),
           ('Interestelar', [2014, 169, 9.5]))



print("A) Dicionário de Filmes:")


# B) Sobre o dicionário de Filmes:

print("B) OPERAÇÕES COM O DICIONÁRIO")
print("-" * 50)

# a) Mostre os dados do filme 'Titanic'

# b) Mostre os dados de um filme cujo título é fornecido pelo usuário usando get
# trate o caso do filme não existir




# c) Inclua o filme 'Avatar 2' com ano 2022, 192 minutos, nota 8.5


# d) Mostre a nota do filme 'Star Wars' usando get (depois a altere, somando 0,5)


# e) Obtenha o título, ano, duração e nota de um filme cujo titulo foi digitado


# f) Mostre o título dos filmes no dicionário


# g) Acrescente 5 minutos de duração aos 3 primeiros filmes (considerando a ordem alfabética do título)

# h) Construa uma tupla com o ano médio e a nota média dos filmes


# i) Construa um dicionário com o título e a categoria da nota (Excelente, Muito Bom, etc) de cada filme


# j) Atualize o dicionário dFilmes com o seguinte dicionário:
print("\nj) Atualizando com novos filmes:")
d2 = {'Duna': [2021, 155, 8.5], 
      'Barbie': [2023, 114, 7.5]}
print("d2 =", d2)


# k) Retire o filme 'Avatar 2' exibindo seus dados

#Contexto: Catálogo de Filmes com Consulta Cruzada (versão simples)


# Dicionário de diretores (chave: título, valor: diretor)
dDiretores = {
    'Matrix': 'Irmãos Wachowski',
    'Titanic': 'James Cameron',
    'Avatar': 'James Cameron',
    'Star Wars': 'George Lucas',
    'O Rei Leão': 'Roger Allers',
    'Interestelar': 'Christopher Nolan'
}

# CONSULTAS CRUZADAS
print("\n" + "="*50)
print("CONSULTAS CRUZADAS")
print("="*50)


# f) Mostre o título e o diretor de todos os filmes


# g) Mostre todos os filmes de um determinado diretor
