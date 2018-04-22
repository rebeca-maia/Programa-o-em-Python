from math import fabs

def mcCarthy(n):
    if n > 100:
        return n - 10
    return mcCarthy(mcCarthy(n+11))

if __name__=='__main__':
    n=int(input("Digite um numero: "))
    i=n-101 #número de chamadas recursivas
    #usas-se 101 porque ele é o ultimo número que, computado na função mcCarthy(n), retorna 91
    print(mcCarthy(n))
    print(fabs(i))
