from math import log10
from math import floor
import numpy as np
#Lei de Benford

def benfordLaw():
    #calcula, para numeros de 1 a 9, a sua probabilidade
    return [log10(1+1.0/i) for i in range(1,10)]

#usa a sequencia de fibonacci para testar se ela segue a lei de benford
def fibonacci(n):
    f=np.empty([n])
    f[0]=1
    f[1]=1
    for i in range(2,n):
        f[i]=f[i-1]+f[i-2]
    return f

#passa um valor da sequencia de fibonacci e extrai o primeiro digito do valor. ex.: 123 -->1
def prim_Dig(x):
    e=floor(log10(x))
    return int(x*10**-e)

if __name__=='__main__':
    #guarda a frequência de cada dígito (1-->9)
    numDig=np.zeros([9]) #retorna um array com 9 posições preenchidas com 0
    n=1000
    f=fibonacci(n)

    for i in range(n):
        j=prim_Dig(f[i])-1 # extrai o primeiro digito do valor correspondente da sequencia de fibonacci
        numDig[j]=numDig[j]+1 # incrementa o array na posição j com a frequencia de aparição daquele dígito

    total=sum(numDig) #soma a fequencia de todos os dígitos (de 1 a 9)
    prob = numDig / 1.0 * total  # array que guarda a probabilidade  de cada digito
    print(""+str(prob))
    ben=benfordLaw() #aplica a lei de benford




