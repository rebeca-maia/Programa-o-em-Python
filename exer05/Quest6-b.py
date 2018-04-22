import random
n=int(input("Tamanho do array:"))
m=int(input("Quantidade de vezes para permutar: "))

perm=[0]*n

for i in range(n):
    perm[i]=i

tabela=[]
for f in range(n):
    row=[0]*n
    tabela+=[row]
media=0
aux=[0]*n
for k in range(m):
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
                index_min=0
            val_min=perm[index_min]
            tabela[o][l]+=val_min
            aux=tabela[o]
            aux.sort()

media=sum(aux)//len(aux)
print("media: {:d}".format(media))

