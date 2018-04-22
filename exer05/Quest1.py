"""
1. O código a seguir calcula a distribuição de probabilidade exata para a soma de dois dados:
Depois que este código for concluído, probabilities[k] é a probabilidade de que os dados somem k.
Execute experimentos para validar este cálculo simulando n vezes esses dados,
mantendo o controle das freqüências de ocorrência de cada valor quando você calcular
a soma de dois números inteiros aleatórios entre 1 e 6.
Como grande não n tem que ser antes de seus resultados empíricos correspondem aos resultados exatos Com três casas decimais?
"""
probabilities = [0.0]*13
n=int(input())
frequency=[]
for l in range(0,13):
    frequency+=[0.0]
for a in range(0,n):
    for i in range(1, 7):
        for j in range(1, 7):
            probabilities[i+j] += 1.0
            frequency[i+j] += 1.0

    for k in range(2, 13):
        probabilities[k] /= 36.0
        #print("%.3f"%probabilities[k])
#print(probabilities)
print(frequency)
"""
frequency=[]
for l in range(0,13):
    frequency+=[0.0]

for i in range(1, 7):
    for j in range(1, 7):
        probabilities[i + j] += 1.0
        frequency[i+j]+=1

for k in range(2, 13):
    probabilities[k] /= 36.0
    #print("%.3f"%probabilities[k])
#print(frequency)
"""