from math import factorial
from math import log
from random import uniform
import numpy as np
"""
Componha uma versão do getCoupon () que usa binomial () do exercício anterior
para retornar valores de cupom de acordo com a distribuição binomial com p = 1/2.
Dica: Gere um número aleatório uniformemente distribuído x entre 0 e 1, depois devolva
o menor valor de k para o qual a soma de f (n, j, p) para todo j <k excede x.

"""
def binomial(k,n,p):
    total1=((p**k)*((1-p)**(n-k))*factorial(n))/(factorial(k)*factorial((n-k)))
    #para evitar inteiros grandes
    f=log(total1)
    return f

def getCoupon(k,n):
    x=uniform(0,1)
    a=list()
    j=0
    g=0
    while j<k:
        b=binomial(n,j,0.5)
        g+=b
        if g >x:
            a[j]=k
        j+=1
    return np.amin(a)

if __name__=='__main__':
    k=int(input("digite um valor para k:"))
    n= int(input("digite um valor para n:"))
    r=getCoupon(k,n)
    print(r)