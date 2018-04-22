"""
Modifique beckett.py para escrever o código Gray, e não apenas a seqüência de posições de bit que mudam.
"""

def genGrayCode(n):
    if n == 1:
        return ['0', '1']
    else:
        lastCode = genGrayCode(n - 1)
        rLastCode = lastCode[:]
        rLastCode.reverse()
        lastCode = [x+ '0' for x in lastCode]
        rLastCode = [x+ '1' for x in rLastCode]
        return lastCode + rLastCode


if __name__=='__main__':
    #n = int(input("Digite um numero:"))
    print(genGrayCode(4))
