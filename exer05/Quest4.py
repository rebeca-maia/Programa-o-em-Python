"""
4.Suponha que você escolha um número inteiro aleatório entre 0 e n-1 no
nosso código de embaralhamento em vez de um entre i e n-1.
Mostre que a ordem resultante não é igualmente provável que seja um dos n! Possibilidades.
Execute o teste do exercício anterior para esta versão.
"""
import random
m=int(input("Tamanho do array: "))
n=int(input("Numero de vezes para embaralhar: "))
#SUITS = ['Clubs','Diamonds','Hearts','Spades']
#RANKS = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']

#rank = random.randrange(0,len(RANKS))
#suit = random.randrange(0,len(SUITS))

a=[]

for i in range(m):
    a+=[i]

tabela=[]
for f in range(m):
    row=[0]*m
    tabela+=[row]

prob=[]

for b in range(m):
    row=[0]*m
    prob+=[row]

for j in range(n):
    for k in range(m):
        r=random.randrange(0,m)
        print("Origem: %d Destino: %d" % (r, k))
        temp=a[r]
        a[r]=a[k]
        a[k]=temp
        tabela[r][k]+=1

for o in range(m):
    for l in range(m):
        prob[o][l] += ((tabela[o][l]) /(n*m))

print(prob)
print(tabela)