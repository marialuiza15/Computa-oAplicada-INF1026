# Utilizando a classe horário e o registro de ponto dos estagiários armazenado na lista
# abaixo:
# Cada elemento desta lista representa: código do estagiário, dia, horário de entrada e
# horário de saída
# Construa um dicionário cuja chave é código do estagiário e o valor é o tempo total trabalhado
# pelo estagiário no formato ( h: m:s).
# Exiba o dicionário construído.

from classeUnidadeTempo import *

def main():
    lPontos = [ (20,1,'10:00','11:10'),
                (20,1,'16:50','18:00'),
                (30,1,'10:00','15:00'),
                (40,1,'15:00','18:00'),
                (20,2,'10:00','18:00'),
                (30,2,'10:00','15:00'),
                (40,2,'08:00','12:10'),
                (20,3,'16:00','17:00'),
                (30,3,'10:00','15:00'),
                (40,3,'15:00','20:00'),
                (20,5,'12:00','15:00'),
                (30,5,'08:00','10:00'),
                (30,5,'12:00','18:00')
                ]
    d = {}
    for estagiario in lPontos:
        codigo = estagiario[0]
        dia = estagiario[1]
        entrada = estagiario[2]
        saida = estagiario[3]

        if codigo not in d:
            d.update({
                codigo: Horario()
            })
        
        if codigo in d:
            h2 = int(saida[0:2])
            h1 = int(entrada[0:2])
            m2 = int(saida[3:5])
            m1 = int(entrada[3:5])

            horario1 = Horario(h1,m1)
            horario2 = Horario(h2,m2)

            diff = horario2 - horario1

            d[codigo] = d.get(codigo) + diff

            print(codigo, horario2 - horario1)
    
    print(d)





main()