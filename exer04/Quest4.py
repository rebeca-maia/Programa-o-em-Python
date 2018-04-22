"""
Modifique sua solução para o exercício anterior para que ele tome dois argumentos de linha de comando n e k,
e escreve todos os P (n, k) = n! / (N-k)! Permutações que contêm exatamente k dos n elementos.
"""
def permutacao(s,k):
    if len(s) == 0:
        return (' ')
    if k > len(s):
        return (' ')
    strings = []

    for i in range(len(s)):
        subStrings = permutacao(s[:i]+s[i+1:],k-1)

        for subString in subStrings:
            #adiciona s[i] à primeira subString; strings=a+bc e a+cb, e assim por diante
            strings += [s[i] + subString]
    return strings


def writeStrings(strings):
    for s in strings:
        if s == '':
            print("empty")
        else:
            print(s)

if __name__=='__main__':
    n=int(input("Digite um numero: ")) #quantidade de letras
    k=int(input("Digite um numero: ")) #tamanho da string,
    alf=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    string=alf[:n]
    strings = permutacao(string,k)
    writeStrings(strings)
