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