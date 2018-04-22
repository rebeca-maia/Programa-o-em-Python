from math import exp
from math import sqrt
from math import pi
from math import log

"""
A fórmula Black Scholes fornece o valor teórico de uma opção de compra europeia sobre uma ação que não paga dividendos,
dado o preço atual das ações s, o preço de exercício x, a taxa de juros livre de risco composta continuamente r,
o desvio padrão σ do estoque Retorno (volatilidade) eo tempo (em anos) até o vencimento t.
O valor é dado pela fórmula sΦ (a) - xe-rtφ (b), onde Φ (z) é a função de distribuição cumulativa gaussiana,
a = (ln (s / x) + (r + σ2 / 2) / (Σt1 / 2), e b = a - σt1 / 2.
Componha um programa que tome s, x, r, sigma e t da linha de comando e escreva o valor Black-Scholes.
Por enquanto, copie as definições das funções phi () e Phi () de gauss.py para o seu programa.
"""

def phi1(x):
    return exp(-x * x / 2.0) / sqrt(2.0 * pi)

#retorna o valor de phi1
def pdf(x, mu=0.0, sigma=1.0):
    return phi1((x - mu) / sigma) / sigma

#depende do valor de phi1
def phi2(z):
    if z < -8.0:
        return 0.0
    if z > 8.0:
        return 1.0
    total = 0.0
    term = z
    i = 3
    while total != total + term:
        total += term
        term *= z * z / float(i)
        i += 2
    return 0.5 + phi1(z) * total


#retorna o valor de phi2
def cdf(z, mu=0.0, sigma=1.0):
    return phi2((z - mu) / sigma)

#calculo final

def blackscholes(s,x,r,sigma,t):
    a = (log(s / x) + (r + (sigma ** 2) / 2) * t) / (sigma * (t ** (1 / 2)))
    b = a - sigma * (t ** (1 / 2))
    return s*phi2(a)-(x**-(r*t))*phi1(b)

if __name__=='__main__':
    s=float(input("Preco atual das acoes:"))
    x=float(input("Preco do exercicio: "))
    r=float(input("Taxa de juros composta livre de risco: "))
    sigma=float(input("Desvio padrao do estoque: "))
    t=float(input("Tempo em anos até o vencimento: "))

    d=blackscholes(s,x,r,sigma,t)
    print(d)


