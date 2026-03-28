# -*- coding: utf-8 -*-

'''
Construa uma função que receba uma palavra no alfabeto latino e
as relações expressas na tuplas tGregoMaiNome, tLatinoGregoMinusculo,
e tGregoMinMai. Para cada caracter desta palavra com correspondência no alfabeto grego
 mostre-o em minúsculo, maiúsculo e nome. Quando não há correspondência,
 exibir mensagem
 Exemplo: Palavra recebida: pago
          p -- min: π   mai: p  nome:pi
          a -- min: α   mai: Α  nome:alfa
          g -- sem correspondência
          o -- min: o   mai: Ο  nome:ômicron
''' 

def tradução(palavra,tGregoMaiNome,tLatinoGregoMinusculo,tGregoMinMai):
    #converte as tuplas em dicionarios pára busca rapida
    latino_para_grego_min = dict(tLatinoGregoMinusculo)
    grego_min_para_mai = dict(tGregoMinMai)
    grego_mai_para_nome = dict(tGregoMaiNome)

    resultado = {}

    for letra in palavra:
        if letra in latino_para_grego_min:
            gregomin = latino_para_grego_min.get(letra, "letra minuscula desconhecida")
            if gregomin in grego_min_para_mai:
                gregomai = grego_min_para_mai.get(gregomin, "letra maiuscula desconhecido")
                nome = grego_mai_para_nome.get(gregomai,"nome desconhecido")
                resultado.update({
                    letra: {'minusculo': gregomin, 'maisculo': gregomai, 'nome':nome}
                })
        else:
            resultado.update({
                letra: "sem correspondencia"
            })
        
            
    return resultado

    
tGregoMaiNome=(('Α','alfa'),('B','beta'),('Γ','gama'),('Δ','delta'),
               ('Ε','épsilon'),('Ζ','dzeta'),('Η','eta'),('Θ','teta'),
               ('Ι','iota'),('Κ','capa'),('Λ','lambda'),('M','mü'),
               ('N','nü'),('Ξ','ksi'),('Ο','ômicron'),('Π','pi'),
               ('Ρ','rô'),('Σ','sigma'),('Τ','tau'),('Υ','upsilon'),
               ('Φ','fi'),('Χ','qui'),('Ψ','psi'),('Ω','ômega'))

tLatinoGregoMinusculo = (('a','α'),('b','β'),('c','γ'),('d','δ'),
                          ('e','ε'),('z','δ'),('ê','η'),('t','θ'),
                          ('j','ι'),('k','k'),('L','λ'),('m','μ'),
                          ('n','ν'),('x','ξ'),('o','ο'),('p','π'),
                          ('r','ρ'),('s','σ'),('t','τ'),('u','υ'),
                          ('f','φ'),('qu','χ'),('ps','ψ'),('ô','ω'))
tGregoMinMai=(('α','Α'),('β','B'),('γ','Γ'),('δ','Δ'),
              ('ε','Ε'),('δ','Ζ'),('η','Η'),('θ','Θ'),
              ('ι','Ι'),('k','Κ'),('λ','Λ'),('μ','M'),
              ('ν','N'),('ξ','Ξ'),('ο','Ο'),('π','Π'),
              ('ρ','Ρ'),('σ','Σ'),('τ','Τ'),('υ','Υ'),
              ('φ','Φ'),('χ','Χ'),('ψ','Ψ'),('ω','Ω'))


print(tradução('malu',tGregoMaiNome,tLatinoGregoMinusculo,tGregoMinMai))