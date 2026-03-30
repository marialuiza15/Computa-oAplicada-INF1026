Estrutura básica    
    d = {"chave": valor}


Regras das CHAVES
    Devem ser imutáveis
        str, int, float, tuple
    Não pode:
        list, dict, set

Tamanho
    len(dict)

Acesso seguro
    d["chave"]      # erro se não existir
    d.get("chave")    # seguro (retorna None)

Percorrer dicionário
    Só chaves:
        for chave in d:
    Chave + valor:
        for chave, valor in d.items():
    Só valores:
        for valor in d.values():

Remoção
    del d["a"]   # direto (pode dar erro)
    d.pop("a")      # seguro
    d.pop("a", None)   # mais seguro ainda
    d.popitem()      # último item

Ordenação (MUITO COBRADO)
    Por chave:
        sorted(d.items())
    Por valor:
        sorted(d.items(), key=lambda x: x[1])


Criar rápido (comprehension)
    d = {i: i**2 for i in range(5)}


Verificar existência
    if "chave" in d:

Métodos importantes
    d.keys()      # chaves
    d.values()    # valores
    d.items()     # pares (chave, valor)

“Eu quero acessar por chave ou por posição?”

posição → lista
chave → dicionário

Cria um dicionário de frequência
frequencia = Counter(itens)

Você pode usar essas tuplas como chave em um dicionário:

d = {}
for t in tupla_de_tuplas:
    d[t] = "valor qualquer"
print(d[('e', 'f')])

modelo padrão (simples e correto) para inverter chave e valor de um dicionário
def inverter_dict(d):
    novo_dict = {}

    for chave, valor in d.items():
        novo_dict[valor] = chave

    return novo_dic


d = {'a': 1, 'b': 2, 'c': 3}
invertido = inverter_dict(d)
print(invertido)
{1: 'a', 2: 'b', 3: 'c'}


SETDEFAULT
d.setdefault('a', [])
- o valor padrão só é usado se a chave NÃO existir
- se já existir, ele ignora completamente o valor passado

SETDEFAULT COM INTEIROS
def contar_palavras(lista):
    d = {}
    for palavra in lista:
        d[palavra] = d.setdefault(palavra, 0) + 1

    return d

SETDEFAULT COM LISTAS
def inverter_jogadores_por_jogo(jogadores):
    novo_dict = {}

    for id_player, (idJogo, rank) in jogadores.items():
        novo_dict.setdefault(idJogo, []).append(id_player)

    return novo_dict


SETDEFAULT COM STRINGS
d = {}

d.setdefault('nome', 'desconhecido')
print(d)


SETDEFAULT COM DICIONARIOS EM DICIONARIOS
d = {}

d.setdefault('usuario1', {}).setdefault('idade', 0)

print(d)

SETDEFAULT COM LISTA DENTRO DE DICIONARIOS
d = {}

d.setdefault('grupo', []).append(1)
d.setdefault('grupo', []).append(2)

print(d)



Remover duplicados COM SET
lista = [1, 2, 2, 3, 3, 3]
sem_repeticao = set(lista)

print(sem_repeticao)

Evitar duplicatas ao agrupar
d = {}

dados = [('a', 1), ('a', 1), ('a', 2)]

for chave, valor in dados:
    d.setdefault(chave, set()).add(valor)

print(d)

Saída:
{'a': {1, 2}}