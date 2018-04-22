from math import log
"""
Componha um programa que define três funções harmonic (), harmonicSmall () e harmonicLarge ()
para calcular os números harmônicos. A função harmonicSmall () deve apenas calcular a soma,
a função harmonicLarge () deve usar a aproximação Hn = log e(n) + γ + 1 / (2n) - 1 / (12n2) + 1 / (120n4)
(o número γ = .5772 ... é conhecido como a constante de Euler),
e a função harmonic () deve chamar harmonicSmall() para n <100 e harmonicLarge() caso contrário.
"""

def harmonic_small(n):
    total1=0
    for i in range(1,n+1):
        total1+=1.0/i
    return total1

def harmonic_large(n):
    y=0.5772156649
    total2=0
    for i in range(1,n+1):
        total2=log(n)+y+(1/(2*n))-(1/(12*(n**2)))+(1/120*(n**4))
    return total2

def harmonic(n):
    if n<100:
        a=harmonic_small(n)
        return a
    else:
        b=harmonic_large(n)
        return b

if __name__=='__main__':
    n = int(input("Digite um numero: "))
    t=harmonic(n)
    print(t)