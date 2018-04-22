from math import gcd

#A função totiente de Euler é uma função importante na teoria dos números: φ (n) é definido como o
# número de inteiros positivos menores ou iguais a n que são relativamente primos com n.
#Componha uma função que leva um argumento inteiro n e retorna φ (n).

def phi(x):
    i = 0
    for n in range(x + 1):
        if gcd(n, x) == 1:
            #print("phi(" + str(x) + ")= " + str(n))
            i+=1
    print("phi(" + str(x) + ")= " + str(i))

if __name__=='__main__':
    x = int(input("Digite um numero: "))
    phi(x)

