"""
5.Reprodução aleatória de música. Ajuste o leitor de música para o modo aleatório.
Ele toca cada uma das m canções antes de repetir qualquer.
Componha um programa para estimar a probabilidade de não ouvir nenhum par seqüencial de músicas
(ou seja, a música 3 não segue a música 2, a música 10 não segue a música 9 e assim por diante).
"""
import random
m=int(input("Tamanho do array: "))
#SUITS = ['Clubs','Diamonds','Hearts','Spades']
#RANKS = ['2','3','4','5','6','7','8','9','10','Jack','Queen','King','Ace']

#rank = random.randrange(0,len(RANKS))
#suit = random.randrange(0,len(SUITS))

a=[]

for i in range(m):
    a+=[i]

tabela=[] #frequencia
for f in range(m):
    tabela+=[0]

prob=[]

for b in range(m):
    prob+=[0]


for k in range(m):
    r=random.randrange(0,m)
    temp=a[r]
    a[r]=a[k]
    a[k]=temp


for z in range(1,m):
    if abs(a[z]-a[z-1])==1:
        tabela[z]+=1

total=0
for t in range(m):
    prob[t] += 1-((tabela[t])/m)
    total+=prob[t]

print(prob)
print("{:.2f} %".format(total*10))