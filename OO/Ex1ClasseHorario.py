# Utilizando a classe horário e a lista de ligações (hora de início e hora de término)
# realizadas por uma pessoa, mostre o tempo total que a pessoa gastou em ligações.
# Cada elemento desta lista é uma tuplinha que representa: horário do início da ligação
# e o horário de término da ligação


from classeUnidadeTempo import *

def main():
    
    lLigacoes = [
        ('08:00','08:10'),('09:50','10:10'),('10:15','11:00'),('12:00','13:00'),('13:50','14:15'),('16:00','17:00'),('17:00','18:15')
        ]
    
    for i,ligacao in enumerate(lLigacoes):
        horario1 = Horario(int(ligacao[0][0:2]),int(ligacao[0][3:5]))
        horario2 = Horario(int(ligacao[1][0:2]),int(ligacao[0][3:5]))
        print(f"A {i+1}° pessoa gastou {horario1+horario2}h")

    return

main()