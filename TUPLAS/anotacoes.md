Estrutura básica
    t = (1, 2, 3)

PRINCIPAL REGRA: é IMUTÁVEL
    Depois de criada, não pode mudar

Tupla com 1 elemento (pegadinha clássica)
    t = (5,)   # tupla
    t = (5)    # é int
    A vírgula é obrigatória!

Tamanho
    len(t)

Acesso aos elementos
    t[0]    # primeiro
    t[-1]   # último

Percorrer tupla
    for x in t:
        print(x)

Desempacotamento (MUITO COBRADO)
    t = (1, 2, 3)
    a, b, c = t
    Resultado:
        a = 1
        b = 2
        c = 3

Desempacotamento com *
    t = (1, 2, 3, 4)
    a, *b = t
    Resultado:
        a = 1
        b = [2, 3, 4]

Concatenação
    t1 = (1, 2)
    t2 = (3, 4)
    t3 = t1 + t2
    
Repetição
    t = (1, 2) * 3
    # (1, 2, 1, 2, 1, 2)

Converter tipos
    list(t)   # tupla → lista
    tuple(l)  # lista → tupla
    Usado pra “modificar” indiretamente

Remoção
    Não pode remover direto
    Mas pode:
        del t   # apaga a tupla inteira

Métodos (poucos!)
    t.count(2)   # quantas vezes aparece
    t.index(2)   # posição

Erros clássicos (CAEM MUITO)
    Tentar modificar
        t[0] = 10   # erro
    Esquecer vírgula
        t = (5)   # int
    Confundir com lista
        t.append(10)   # NÃO EXISTE 

Tupla pode ter elementos mutáveis
    t = ([1,2], 3)
    t[0].append(4)   #  funciona
    A tupla é imutável, mas o conteúdo pode não ser

Quando usar tupla?
    Dados fixos
    Segurança (não pode alterar)
    Retorno de múltiplos valores

Retorno múltiplo de função
    def f():
        return 1, 2
    x, y = f()