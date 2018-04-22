from math import factorial
"""
Componha um programa de constrói e escreve uma matriz bidimensional irregular A tal que A[n][k] contém a probabilidade
de que você obtenha exatamente 5 caras quando você joga uma moeda n vezes. Tome um argumento da linha de comando para especificar
o máximo valor de n. Estes números são conhecidos como a distribuição binomial.
"""

n=int(input())
k=int(input())
binomial=[]
r=1
for y in range(n):
    linha=[1]*r
    binomial+=[linha]
    r+=1

for i in range(n):
    for j in range(i):
        binomial[i][j]=[(factorial(i)/(factorial(j)*factorial(i-j)))*(0.5**j)*(0.5**(i-j))]
        if j==0:
            binomial[i][j]=1

for row in binomial:
    for v in row:
        print(v,end=' ')
    print()

print(binomial[n-1][k-1])

