"""
3.Verificação aleatória empírica. Execute experimentos computacionais
para verificar se o nosso código de embaralhamento funciona como esperado.
Componha um programa que tome os argumentos m e n da linha de comando, faz n shuffles
de um array de tamanho m que é inicializada com a[i] = i antes de cada shuffle
e cria uma tabela m-by-m de tal forma que a linha i Dá o número de vezes que i acabou
na posição j para todos os j.
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

for j in range(n):
    for k in range(m):
        r=random.randrange(k,m)
        print("Origem: %d Destino: %d"%(r,k))
        temp=a[r]
        a[r]=a[k]
        a[k]=temp
        tabela[r][k]+=1

print(tabela)