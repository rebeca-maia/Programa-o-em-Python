"""
#1118
import sys
cont=0
a=[]
while True:
    try:
        m=float(input())
    except EOFError:
        break
    if 0.0<=m<=10.0:
        a+=[m]
        cont+=1
        if cont==2:
            media=(a[0]+a[1])/2
            print("media = %.2f"%media)
            while 1:
                x=int(input("novo calculo (1-sim 2-nao)"))
                if x==1:
                    break
                elif x==2:
                    sys.exit(0)
                elif (x!=2) and (x!=1):
                    pass
                cont=0
            a.clear()
    else:
        print("nota invalida")

#1131
import sys

def jogo():
    cont, e, vi, vg = 0, 0, 0, 0
    while 1:
        l=input()
        s=l.split()
        inter=int(s[0])
        gre=int(s[1])
        if inter ==gre:
            e+=1
            cont+=1
        elif inter>gre:
            vi+=1
            cont+=1
        elif gre>inter:
            vg+=1
            cont+=1
        while 1:
            x=int(input("Novo grenal (1-sim 2-nao)"))
            if x==2:
                print("%d grenais\nInter:%d\nGremio:%d\nEmpates:%d"%(cont,vi,vg,e))
                if vi>vg:print("Inter venceu mais")
                elif vg>vi:print("Gremio venceu mais")
                elif vi==vg: print("Nao houve vencedor")
                sys.exit(0)
            elif (x!=2) and (x!=1):
                pass
            elif x==1:
                break



if __name__=='__main__':
    jogo()

#1145
l=input()
z=l.split()

X=int(z[0])
Y=int(z[1])
cont=0
if 1<X<20 and X<Y<100000:
        for i in range(1,Y+1):
            if (i%(X+1))==0:
                print("\n")
            else:
                print(i,end=' ')
        print("\n")


#1149
v=input()
s=v.split()
A=int(s[0])
N=int(s[1])
t=0
if N<=0:
    while 1:
        B = int(input())
        N = B
        if N<=0:
            pass
        else:
            for j in range(A, A + N):
                t += j
            print(t)
            break
else:
    for i in range(A,A+N):
        t+=i
    print(t)

#1150
X=int(input())
Z=int(input())
t=0

if Z<=X:
    while 1:
        A=int(input())
        Z=A
        k=0
        i=X
        if Z<=X:
            pass
        else:
            while t<Z:
                t+=i
                k+=1
                i+=1
            print(k)
            break
else:
    u=0
    j=X
    while t<Z:
        t+=j
        u+=1
        j+=1
    print(u)


#1160
from decimal import *

T=int(input())

if 1<=T<=3000:
    for i in range(T):
        l=input()
        s=l.split()
        PA=int(s[0])
        PB=int(s[1])
        getcontext().prec=1
        G1=float(s[2])
        G2=float(s[3])
        if (100<=PA<=1000000) and (PA<PB<=1000000) and (0.1<=G1<=10.0) and (0.0<=G2<=10.0) and (G2<G1):
            G1/=100
            G2/=100
            anos=0
            while not PA>PB:
                PA+=int(PA*G1)
                PB+=int(PB*G2)
                anos += 1
            if anos >100:
                print("Mais de 1 seculo.")
                break
            else:
                print("%d anos."% anos)

#1164
N=int(input())

if 1<=N<=20:
    for i in range(N):
        X=int(input())
        if 1<=X<=(10**8):
            t = 0
            for j in range(1,X):
                if X%j==0:
                    t+=j
            if t==X: print("%d eh perfeito"%X)
            else: print("%d nao eh perfeito"%X)

#1165
N=int(input())
if 1<=N<=100:
    for j in range(N):
        X=int(input())
        if 1<X<=(10**7):
            d=0
            for i in range(1,X+1):
                if X%i==0:
                    d+=i
            if d==X+1:
                print("%d eh primo"%X)
            else:
                print("%d nao eh primo"%X)

#1172
X=[]
for i in range(10):
    x=int(input())
    if x<=0:
        X+=[1]
    else:
        X+=[x]
    print("X[%d] = %d"%(i,X[i]))

#1173
V=int(input())
if V<=50:
    N=[]
    u=V
    for i in range(10):
        N+=[u]
        u*=2
        print("N[%d] = %d"%(i,N[i]))

#1175
N=[]
for i in range(5):
    s=int(input())
    N+=[s]

k=len(N)-1
for j in range(5):
    temp=N[j]
    N[j]=N[k]
    N[k]=temp
    k-=1

for a in N:
    print(a)

#1176
T=int(input())
f=[]
for i in range(T):
    N=int(input())
    if 0<=N<=60:
        if N<2:
            for i in range(N+1):
                f+=[i]
        else:
            f=[0]*(N+1)
            f[0]=0
            f[1]=1
            for j in range(2,N+1):
                f[j]=f[j-1]+f[j-2]
        print("Fib(%d) = %d"%(N,f[N]))

#1177
T=int(input())
if 2<=T<=50:
    N=[]
    for i in range(1000):
        aux=i%T
        N+=[aux]
        print("N[%d] = %d"%(i,N[i]))

#1178
from decimal import *
getcontext().prec=4
X=float(input())
N=[]
a=X
for i in range(100):
    N+=[a]
    a/=2
    print("N[%d] = %.4f"%(i,N[i]))

#1179
par=[0]*5
impar=[0]*5
tras,aux=0,0
back,he=0,0
for i in range(15):
    X=int(input())
    if X%2!=0:
        if (back+1)%5==0:
            impar[back]=X
            back=(back+1)%5
            for k in range(len(impar)):
                print("impar[%d] = %d"%(k,impar[k]))
            he+=1
        else:
            impar[back]=X
            back = (back + 1) % 5
            he+=1
    else:
        if (tras+1)%5==0:
            par[tras]=X
            tras=(tras+1)%5
            for j in range(len(par)):
                print("par[%d] = %d"%(j,par[j]))
            aux+=1
        else:
            par[tras]=X
            tras = (tras + 1) % 5
            aux+=1

for m in range((he-5)%5):
        print("impar[%d] = %d" % (m, impar[m]))

for l in range((aux - 5)%5):
    print("par[%d] = %d" % (l, par[l]))

#1180
N=int(input())
p=input()
s=p.split()
if 1<N<1000 and len(s)==N:
    X=list(map(int,s))
    val_min=min(X)
    index_min=X.index(val_min)
    print("Menor valor: %d\nPosicao: %d"%(val_min,index_min))

#1181
L=int(input())

if 0<=L<=11:
    T=input()
    M = [[float(input()) for i in range(12)] for j in range(12)]
    s = 0
    for k in range(12):
        for l in range(12):
            if k == L:
                s += M[k][l]
    if T=='S':
        print("%.1f"%s)
    if T=='M':
        m=s/12
        print("%.1f"%m)

#1182
C=int(input())

if 0<=C<=11:
    T=input()
    M = [[float(input()) for i in range(12)] for j in range(12)]
    s = 0
    for k in range(12):
        for l in range(12):
            if l == C:
                s += M[k][l]
    if T=='S':
        print("%.1f"%s)
    if T=='M':
        m=s/12
        print("%.1f"%m)

#1183

O=input()
M = [[float(input()) for i in range(12)] for j in range(12)]
s = 0
for k in range(12):
    for l in range(12):
        if l > k:
            s+=M[k][l]
if O=='S':
    print("%.1f"%s)
if O=='M':
    m=s/66
    print("%.1f"%m)


#1184
O=input()
M = [[float(input()) for i in range(12)] for j in range(12)]
s = 0
for k in range(12):
    for l in range(12):
        if k > l:
            s+=M[k][l]
if O=='S':
    print("%.1f"%s)
if O=='M':
    m=s/66
    print("%.1f"%m)

#1185
O=input()
M = [[float(input()) for i in range(12)] for j in range(12)]
s = 0
for k in range(12):
    for l in range(12):
        if k +l<=10:
            s+=M[k][l]
if O=='S':
    print("%.1f"%s)
if O=='M':
    m=s/66
    print("%.1f"%m)

#1186
O=input()
M = [[float(input()) for i in range(12)] for j in range(12)]
s = 0
for k in range(12):
    for l in range(12):
        if k +l>=12:
            s+=M[k][l]
if O=='S':
    print("%.1f"%s)
if O=='M':
    m=s/66
    print("%.1f"%m)
#1187
O=input()
M = [[float(input()) for i in range(12)] for j in range(12)]
s = 0
a,l,c=len(M)-2,0,1
while l<=a:
    while c<=a:
        if l<c:
            s+=M[l][c]
        c+=1
    l+=1
    a-=1
if O=='S':
    print("%.1f"%s)
if O=='M':
    m=s/30
    print("%.1f"%m)

#1188
O=input()
M =[[float(input()) for i in range(12)] for j in range(12)]
s=0

for x in range((len(M)//2)+1,len(M)):
    for y in range(12-x,x):
        s+=M[x][y]
if O=='S':
    print("%.1f"%s)
if O=='M':
    m=s/30
    print("%.1f"%m)

#1189
O=input()
M =[[float(input()) for i in range(12)] for j in range(12)]
s=0

for x in range(1,len(M)-1):
    for y in range((len(M)//2)-1):
        s+=M[x][y]
if O=='S':
    print("%.1f"%s)
if O=='M':
    m=s/30
    print("%.1f"%m)

#1190
O=input()
M =[[float(input()) for i in range(12)] for j in range(12)]
s=0
for x in range(1,len(M)-1):
    for y in range((len(M)//2)+1,len(M)):
        s+=M[x][y]
if O=='S':
    print("%.1f"%s)
if O=='M':
    m=s/30
    print("%.1f"%m)
"""
#1435

M=[]
while 1:
    N=int(input())
    if 0<=N<=100:
        if N==0:
            break
        for i in range(N):
            row=[1]*N
            M+=[row]
        for k in range(N):
            for l in range(N):
