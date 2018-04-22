"""
Componha um programa que tenha um argumento inteiro de linha de comando n e
escreva todas as 2^n combinações de qualquer tamanho.
Uma combinação é um subconjunto dos n elementos, independente da ordem.
"""

def combinacao(s):
    strings=[]
    for i in range(len(s)+1):
        strings+=combinacoesDeTamanho(s,i)
    return strings

def combinacoesDeTamanho(s,k):
    if k==0:
        return (' ')
    strings=[]
    for i in range(len(s)):
        subStrings=combinacoesDeTamanho(s[i+1: ],k-1)
        for subString in subStrings:
            strings+=[s[i]+subString]
    return strings

def writeStrings(strings):
    for s in strings:
        if s == '':
            print("empty")
        else:
            print(s)

if __name__=='__main__':
    n=int(input("Digite um numero: "))
    alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
    string = alf[:n]
    strings = combinacao(string)
    writeStrings(strings)