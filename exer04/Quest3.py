"""
Componha um programa que toma um argumento de linha de comando n e escreve todas as n! Permutações
das n letras começando em a (suponha que n não é maior que 26).
Uma permutação de n elementos é um dos n! Possíveis ordenações dos elementos.
Não se preocupe com a ordem em que você irá enumerá-los.
"""

def permutacao(s):
    if len(s) == 0:
        return (' ')
    strings = []
    for i in range(len(s)):
        #quando s[i]==a, subStrings=[bc], quando s[i]==b,subStrings=[ac],quando s[i]==c,subStrings=[ab]
        print(s)
        print(s[:i] + s[i + 1:])
        subStrings = permutacao(s[:i]+s[i+1:])

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
    n=int(input("Digite um numero: "))
    alf=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    string=alf[:n]
    strings = permutacao(string)
    writeStrings(strings)