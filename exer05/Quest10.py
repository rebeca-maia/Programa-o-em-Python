from random import randrange
"""
Dada uma matriz de n elementos com cada elemento entre 1 e n, compor um fragmento de código para determinar se existem
quaisquer duplicatas. Você não precisa preservar o conteúdo da matriz fornecida, mas não use uma matriz extra.
"""

n=int(input())
m=[]
r=0
for i in range(n):
    r=randrange(1,n+1)
    m+=[r]

for u in m:
    print(u,end=' ')
print("\n")
c=1
for j in range(len(m)):
    ig=m[j]
    for k in range(c,len(m)):
        if ig==m[k]: #a primeira e seguintes ocorrências de um número repetido, ele é atribuído zero(menos sua última ocorrência)
            m[j]=0
    c+=1

for l in m:
    if l!=0:
        print(l,end=' ')