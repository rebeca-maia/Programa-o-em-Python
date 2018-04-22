from math import factorial
from math import log
from math import exp
from math import sqrt
from math import pi
from math import fabs
#Distribuição Binomial
def binomial(k,n,p):
    #Calcula a probabilidade de obter exatamente k cabeças em n voltas de moedas inclinadas(cabeças com probabilidade p)
    total1=((p**k)*((1-p)**(n-k))*factorial(n))/(factorial(k)*factorial((n-k)))
    #para evitar inteiros grandes
    x=log(total1)
    return x

#para a distribuição normal
def phi(x):
    return exp(-x * x / 2.0) / sqrt(2.0 * pi)

def pdf(x, mu=0.0, sigma=1.0):
    return phi((x - mu) / sigma) / sigma
def Phi(z):
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
    return 0.5 + phi(z) * total

def cdf(z, mu=0.0, sigma=1.0):
    return Phi((z - mu) / sigma)

def dist_normal(k,n,p):
    c1=cdf(k+1/2,n*p,n*p*((1-p)**(1/2)))
    c2=cdf(k-1/2,n*p,n*p*((1-p)**(1/2)))
    total2=c1-c2
    return total2

if __name__=='__main__':
    n=int(input("Informe o algorismo: "))
    k=int(input("Informe o algorismo: "))
    p=float(input("Informe o algarismo: "))
    f1=binomial(k,n,p)
    f2=dist_normal(k,n,p)
    #Comparar o valor dos dois
    print(fabs(f1))
    print(f2)

