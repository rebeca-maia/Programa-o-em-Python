import sys
"""
Componha um programa que aceita a permutação de inteiros entre 0 e n-1, sendo que n é informado como argumento da linha de comando,
e escreve seu inverso.(Se a permutação é um array a[], seu inverso é um array b[], tal que a[b[i]]=b[a[i]]=1). Verifique se é uma
válida permutação.
"""
def permutacao(a1):
    if len(a1)==0:
        return (' ')
    a2=[]
    for j in range(len(a1)):
        aux=permutacao(a1[:j]+a1[j+1:])
        for el in aux:
            a2+=[a1[j]+" "+el]
    return a2


if __name__=='__main__':
    n=int(input())
    a=[]
    b=[]
    for i in range(n):
        a+=[input()]

    answer=permutacao(a)
    for s in answer:
        print(s)
    print("\n")

    b = a[:]
    ans=permutacao(b)

    for n in ans:
        print(n)
