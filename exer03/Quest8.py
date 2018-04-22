from math import factorial
from math import exp
import numpy as np
#Método de Horner
#Componha um programa com a função avalie(x,a) que avalia o polinômio a(x) cujos coeficientes são
#os elementos na matriz a[]: a0+a1*x^1+...+an-1*x^n-1
#Use o método de Horner,uma maneira eficiente para melhorar a performance do algoritmo.
#Então componha a função exp(), que chama avalie() para computar uma aproximação à e^x, usando
#os n primeiros termos da expansão da série de Taylor
#Pegue um argumento x da linha de comando e compare seu resultado contra math.exp(x)


def avalie(x,a):
    sum=0
    for i in range(len(a)):
        sum+=a[i]*(x**i)
    return sum
#-------------------------------
def expo(x):
    soma=0
    for i in range(len(a)):
        b=avalie(x,a)
        soma+=b/factorial(i)
    return soma
if __name__=='__main__':
    x = int(input("Digite o expoente: "))
    n = 10
    a = np.arange(1, n)
    c=expo(x)
    print(c/10000)
    print(exp(x))