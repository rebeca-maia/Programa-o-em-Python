"""
Modifique sua solução do exercício anterior para que ele tome dois argumentos de linha de comando n e k,
e escreva todos as C (n, k) = n! / (K! * (N-k)!) combinações de tamanho k.
"""

def combinacoes(s,k):
    if k==0:
        return (' ')
    strings=[]
    for i in range(len(s)):
        subStrings=combinacoes(s[i+1: ],k-1)
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
    k= int(input("Digite um numero: "))
    alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
    string = alf[:n]
    strings = combinacoes(string,k)
    writeStrings(strings)