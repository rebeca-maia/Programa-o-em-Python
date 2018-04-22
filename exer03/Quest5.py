from math import exp
from math import sqrt
from math import pi
#Questao 5 - funçao de densidade de probabilidade cumulativa inversa de Gauss usando busca binária
"""
Um método geral que estudamos detalhadamente na Seção 4.2 é eficaz para calcular o inverso
de uma função de densidade de probabilidade cumulativa como cdf ().
Tais funções são contínuas e não decrescentes de (0, 0) a (1, 1).
Para encontrar o valor x0 para o qual f (x0) = y0, verifique o valor de f (.5).
Se for maior que y0, então x0 deve estar entre 0 e 0,5; Caso contrário, ele deve estar entre 0,5 e 1.
De qualquer forma, reduzimos para metade o comprimento do intervalo conhecido por conter x0.
Iterando, podemos calcular x0 para dentro de uma determinada tolerância.
Adicione uma função cfdInverse () a gauss.py que usa pesquisa binária para calcular o inverso.
"""

#Devolver o valor da função de probabilidade Gaussiana com média 0,0
#e o desvio padrão de 1,0 ao valor dado x.
#é necessário para calcular phi2
def phi1(x):
    return exp(-x * x / 2.0) / sqrt(2.0 * pi)


#Devolver o valor da função de probabilidade Gaussiana com média mu
#e desvio padrão sigma correspondente ao valor dado x.
#depende do valor de phi1
def pdf(x, mu=0.0, sigma=1.0):
    return phi1((x - mu) / sigma) / sigma


#Devolver o valor da função de distribuição de Gauss cumulativa
#com média 0,0 e desvio padrão 1,0 ao valor dado z.
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

#Devolver o valor da função de distribuição de Gauss cumulativa
#com média mu e desvio padrão sigma no dado valor z.
#depende do valor de phi2
def cdf(z, mu=0.0, sigma=1.0):
    return phi2((z - mu) / sigma)


#depende do valor de phi2
def phi_inverse(y,delta,lo,hi):
    mid = lo + ((hi - lo) / 2.0)
    if (hi-lo)<delta:
        return mid
    if phi2(mid) > y:
        return phi_inverse(y,delta,lo,mid)
    else:
        return phi_inverse(y,delta,mid, hi)

    #phi(x)=y
def PhiInverse(y):
    return phi_inverse(y,0.000000001, -8.0, 8.0)

if __name__=='__main__':
    z=float(input("Digite um valor para descobrir a função f(x)=y: "))
    y=phi2(z)
    x=PhiInverse(y)

    print("f(%.3f" %x,")=%.3f" %y)

