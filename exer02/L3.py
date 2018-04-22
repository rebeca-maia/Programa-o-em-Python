import math
"""
#Questao
# menor número expressível como a soma de dois cubos de duas maneiras diferentes
n = int(input("Digite um numero:"))
a=1
while a <=n:
    a1=a**3
    if a1>n:
        break
    b=a
    while b<=n:
        b1=b**3
        if a1+b1>n:
            break
        c=a+1
        while c<=n:
            c1=c**3
            if c1> a1+b1:
                break
            d=c
            while d<=n:
                d1=d**3
                if c1+d1>a1+b1:
                    break
                if c1+d1 == a1+b1:
                    print(str(n)+"="+str(a1)+"^3+"+str(b1)+"^3="+str(c1)+"^3+"+str(d1)+"^3")
                d+=1
            c+=1
        b+=1
    a+=1

#Questao 2
num=int(input("Digite um numero de 9 digitos: "))
total=0
for i in range(8,10,-1):
    cont = (11 % i)
    if i>cont:
        cont-=1
        total+=num[i]*cont
    if i ==cont:
        total=total+num[i]*i
    if i <cont:
        while 11%i == 1:
            cont+=2
            total+=num[i]*cont


print("O numero completo é: "+str(total))
"""
#Questao 3
#Crivo de Eratóstenes
n=int(input("Digite o tamanho máximo: "))
v=[range(n+1)]

i = 2
while i**2<=n:
    j=i+1
    while j<=n:
        if v[j]!=0 and j%i==0:
            v[j]=0
        j+=1
    j=i+1
    while v[j]==0 and j<=n:
        i=j
        j+=1

for i in range(2,n+1):
    if v[i]!=0:
        print("%i" %i)

#Questão 4
#passos aleatórios
n=int(input("Digite um numero: ")) #numero de passos
i=0 #vertice
cont=0

while i<=n:
    i=i*1/4
    i+=1
    cont+=1
    if i ==(2*n+2*n)**2:
        break

print("numero de passos: "+str(cont))
print("Probabilidade de todo o percurso: "+str(i))

#Questão 5
#Mediana
a=int(input("Digite um numero: "))
b=int(input("Digite um numero: "))
c=int(input("Digite um numero: "))
d=int(input("Digite um numero: "))
e=int(input("Digite um numero: "))

v=[a,b,c,d,e]
#ordena lista
i=0
while i<len(v):
    j=i+1
    while j<=len(v):
        if v[i]>v[j]:
            aux=v[i]
            v[i]=v[j]
            v[j]=aux
        j+=1
    i+=1

#obter mediana
if len(v)%2==1:
    m=math.ceil(len(v)/2)
if len(v)%2==0:
    m=float(len(v)/2)
    m1=float(m+1)
    print((m+m1)/2.0)

#Questao 8
#seno e cosseno série de taylor
#seno
x=float(input("Digite um numero: "))
n=1
total1=0
while n<x:
    total1=((-1)**n)*(x**(2*n+1))/(math.factorial(2*n+1))
    n+=1

#cosseno
n=1
total2=0
while n<x:
    total2=((-1)**n)*(x**(2*n))/2*math.factorial(n)
    n+=1





