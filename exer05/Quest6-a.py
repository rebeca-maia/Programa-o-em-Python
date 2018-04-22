"""
6.Minima em permutações. Componha um programa que toma um inteiro n da linha de comando,
gera uma permutação aleatória, escreve a permutação e o número de mínimos da esquerda para a direita
na permutação (o número de vezes que um elemento é o menor visto até agora).
Em seguida, componha um programa que leva os inteiros m e n a partir da linha de comando,
gera m permutações aleatórias de tamanho n, e escreve o número médio de mínimos da esquerda para a direita nas permutações geradas.
"""
import random
n=int(input())

perm=[0]*n

for i in range(n):
    perm[i]=i

tabela=[]
for f in range(n):
    row=[0]*n
    tabela+=[row]

for k in range(n):
    for j in range(n):
        r=random.randrange(j,n)
        temp=perm[r]
        perm[r]=perm[j]
        perm[j]=temp
        #print(perm)
    for l in range(n):
        index_min=l
        for o in range(l+1,n):
            if perm[o] < perm[index_min]:
                index_min=o
            val_min=perm[index_min]
            tabela[o][l]+=val_min

print(tabela[o])
