# Operações matemáticas múltiplas

# Crie uma função:
# def operacoes(a, b):

# que receba dois números e retorne uma tupla com:
# soma
# subtração
# multiplicação
# divisão

# Exemplo esperado:
# operacoes(8,4)
# (12, 4, 32, 2)

def operacoes(a, b):
    if b==0:
        return (a+b, a-b, a*b, None)
    else:
        return (a+b, a-b, a*b, a/b)