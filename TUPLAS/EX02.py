# Faça uma função ordena que receba três valores inteiros a, b e c e retorna uma tupla com os valores ordenados crescentemente.

#  Os três jurados de um concurso de fantasias avaliam 2 critérios distintos: originalidade e beleza. 
#  A nota final do candidato é calculada do seguinte modo: 0.6 * nota_da_originalidade + 0.4 * nota_da_beleza
#  Para evitar distorções, são desprezadas a maior e a menor nota de cada
# critério. Faça um programa, que leia, para o candidato, o seu número de
# inscrição (inteiro) e suas 3 notas (reais) de cada critério, exibindo sua nota
# final.
#  O seu programa deve, obrigatoriamente, utilizar a função ordena.
# Modificação: Crie um arquivo com o número de inscrição e notas de vários
# candidatos (um candidato por linha com seus dados separados por ‘;’). Altere
# seu programa para utilizá-lo.

def ordena(a,b,c):
    listaAuxiliar = [a,b,c]
    primeiro = 0
    segundo = 0
    terceiro = 0
    for i in listaAuxiliar:
        if i>primeiro:
            segundo = primeiro
            terceiro = segundo
            primeiro = i
        elif primeiro>i>segundo:
            terceiro = segundo
            segundo = i
        elif primeiro>i and segundo>i:
            terceiro = i
    return (terceiro,segundo,primeiro)


def main():
    numInscricao = int(input("Insira o seu numero de inscrição: "))
    nota_da_originalidade1 = float(input("Insira a 1° nota de originalidade: "))
    nota_da_originalidade2 = float(input("Insira a 2° nota de originalidade: "))
    nota_da_originalidade3 = float(input("Insira a 3° nota de originalidade: "))
    nota_originalidade_ordenada = ordena(nota_da_originalidade1,nota_da_originalidade2,nota_da_originalidade3)
    nota_da_beleza1 = float(input("Insira a 1° nota de beleza: "))
    nota_da_beleza2 = float(input("Insira a 2° nota de beleza: "))
    nota_da_beleza3 = float(input("Insira a 3° nota de beleza: "))
    nota_beleza_ordenada = ordena(nota_da_beleza1,nota_da_beleza2,nota_da_beleza3)

    print(f"nota final do candidato {numInscricao}: {0.6*nota_originalidade_ordenada[1] + 0.4*nota_beleza_ordenada[1]}")
    return

main()