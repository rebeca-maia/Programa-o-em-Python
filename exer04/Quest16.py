from math import ceil
from math import floor
"""
Componha um programa que recebe um argumento de linha de comando m e retorna o valor de n < m
para o qual o número de chamadas recursivas para collatz (n) é maximizado.
O problema não resolvido é que ninguém sabe se a função termina para todos os valores positivos de n
(indução matemática não ajuda porque uma das chamadas recursivas é para um valor maior do argumento).
"""
def collatz(n,m):
    print(str(n) + ' ')
    if n < m:
        return
    if n==1:
        return
    fl=floor(n/2)
    ce=ceil(n/2)
    if fl > ce:
        if fl%2 == 0:
            collatz(fl,m)
        else:
            collatz(3*(fl*2)+1,m)
    else:
        if ce% 2 == 0:
            collatz(ce, m)
        else:
            collatz(3 * (ce * 2) + 1, m)

if __name__=='__main__':
    n=int(input("Informe um numero: "))
    m = int(input("Informe um numero: "))

    collatz(n,m)