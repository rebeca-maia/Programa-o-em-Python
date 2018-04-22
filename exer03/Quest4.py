from random import uniform
from math import sqrt
from math import log
from array import array
"""
Experimente a seguinte função para gerar variáveis aleatórias a partir da distribuição gaussiana,
que é baseada na geração de um ponto aleatório no círculo unitário e usando a transformada Box-Muller.
Pegue um argumento de linha de comando n e gere n números aleatórios, usando uma matriz a [] de 20 inteiros para contar
os números gerados entre i * .05 e (i + 1) *. 05 para i de 0 a 19.
"""

def gaussian():
    r = 0.0
    while (r >= 1.0) or (r == 0.0):
        x = uniform(-1.0, 1.0)
        y = uniform(-1.0, 1.0)
        r = x*x + y*y
    return x * sqrt(-2.0 * log(r) / r)

def generateNRandomNumbers(qtt):
    randomNumbers = array('f')
    for it in range(qtt):
        randomNumbers.append(gaussian())
    return randomNumbers

if __name__ == '__main__':
    numbers_qt = int(input("Qual a quantidade de números aleatórios:?"))
    random_list = generateNRandomNumbers(numbers_qt)

    for it in range(20):
        counter = 0
        for number in random_list:
            if (it * .05) < number < ((it+1) * .05):
                counter += 1
                print("Para i igual a " + repr(it) + " temos " + repr(counter) + " números no intervalo.")
                counter = 0