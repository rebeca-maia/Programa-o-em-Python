#Questões 1,3,4,5,6,7,9,11,14,15,16
from array import array

"""
Componha um programa que tome um inteiro positivo n (em decimal) a partir da linha de comando
e escreva sua representação binária. Use o seguinte método: dividir repetidamente n por 2 e ler os remanescentes para trás.
Primeiro, compor um loop while para realizar este cálculo e escrever os bits na ordem errada.
Em seguida, use recursão para gravar os bits na ordem correta.
"""

def binario(n):
    if n==0:
        return
    binario(n//2)
    print(n%2)

if __name__=='__main__':
    n=int(input("Escreva um numero: "))
    binario(n)
