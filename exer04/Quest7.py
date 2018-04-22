"""
A distância de Hamming entre duas strings de bits de comprimento n é igual ao número de bits em que as duas cadeias diferem.
Componha um programa que tome um inteiro k e um bit string s da linha de comando,
e escreve todas as strings de bits que têm Hamming distância no máximo k de s.
"""
def hamming(k,s):
    if k==0:
        return
    else:
        for i in range(len(k)+1):
            total=hamming(k-1,s[i+1:])




if __name__=='__main__':
    k=int(input("Digite um numero:"))
    s=int(input("Digite um binario: "))

