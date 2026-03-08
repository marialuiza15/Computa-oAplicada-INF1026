#valor em caixa
#valor do presente

# Caso o preço do presente seja superior a 80% do valor em caixa, a compra deve ser feita a prazo (5x), com juros de 10% sobre o valor do presente. 
# Caso o presente custe entre 50% e 80% do valor em caixa, a compra deve ser feita a prazo (3x), com juros de 8% sobre o valor do presente. 
# Caso contrário, a compra deverá ser realizada a vista, onde o apaixonado receberá 5% de desconto.

# Seu programa deve capturar o "valor em caixa" e o valor do presente, ativar a função abaixo, e mostrar o número de parcelas e o valor a pagar em cada parcela de acordo com a regra acima.

# Faça uma função que receba o "valor em caixa", o valor do presente e retorne uma tupla com o número de parcelas (1, 3 ou 5) e o valor da parcela.


def calcCustoPresente(valorEmCaixa, valorPresente):
    if valorPresente > valorEmCaixa*0.8:
        parcelas = 5
        total = valorPresente + valorPresente*0.1

    elif valorEmCaixa*0.8 > valorPresente > valorEmCaixa*0.5 :
        parcelas = 3
        total = valorPresente + valorPresente*0.08
        
    else:
        parcelas = 1
        total = valorPresente - valorPresente*0.05

    valorParcela = total/parcelas
    parcelasTotal = (parcelas, valorParcela)
    return parcelasTotal

def main():
    valorEmCaixa = float(input("Insira o valor em caixa: "))
    valorPresente = float(input("Insira o valor do presente: "))

    totalCalculado = calcCustoPresente(valorEmCaixa, valorPresente)

    if totalCalculado[0] == 0:
        print(f"a compra deve ser feita a vista, e o valor de cada parcela será: {totalCalculado[1]}")
        return
    print(f"a compra deve ser feita parcela em {totalCalculado[0]}x, e o valor de cada parcela será: {totalCalculado[1]}")
    return

main()
