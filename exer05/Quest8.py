import numpy as np

def Hadamard(h,indice):
    if indice ==0:
        h[0][0]=1
        return
    Hadamard(h,indice//2)
    copia(h,0,0,indice,indice,0,1)
    copia(h,0,0,indice,0,indice,1)
    copia(h,0,0,indice,indice,indice,-1)

def copia(h,i,j,max,al_i,al_j,invert):
    if j==max:
        j=0
        i+=1
    if i==max:
        return
    h[i+al_i][j+al_j]=h[i][j]*invert
    copia(h,i,j+1,max,al_i,al_j,invert)

def imprimir(h):
    print("{:^16}".format('H(%d)'%len(h)))
    print("----------------")
    for k in range(len(h)):
        for m in range(len(h)):
            if h[k][m]==1:
                print("T",end=' ')
            else:
                print("F",end=' ')
        print()

if __name__=='__main__':
    n=int(input())
    h=np.zeros((n,n))
    Hadamard(h,len(h)//2)
    imprimir(h)
