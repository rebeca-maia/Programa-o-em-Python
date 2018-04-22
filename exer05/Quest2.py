"""
Dada um array de inteiros, componha um programa que localiza o comprimento e
a localização da seqüência contígua mais longa de valores iguais onde
os valores dos elementos antes e depois dessa seqüência são menores.
11133333322
"""
import random
n= 20 #tamanho do array
m= 3 #alcance de numeros aleatorios
cont,size,ind_inic=0,0,0
a=[]

#cria um array de n itens com numeros de 1 a m
for j in range(n):
    a+=[random.randint(1,m)]

i=1 #Começa em 1 porque você estará olhando para o valor anterior a i-1,começando em 0 dará erro
while i<n-2: #Você estará olhando para i + 2, então pare em N-2
#Observe o escopo do que se segue. Enquanto i é menor que N-2, verifique se há uma corrida.
#Se houver uma corrida, conta o seu comprimento e verificar se é um platô.
#Se não houver nenhuma corrida, reinicialize o contador e incremente i.

#Verifique se você tem uma corrida de mesmo número
    if a[i] ==a[i+1]:
        cont+=1 #Se tiver uma corrida, incremente o contador. O contador conta o comprimento de uma corrida

        #Dois testes principais estão aqui:
        #esta corrida é mais longa do que outras corridas anteriores,
        #e é este realmente um plateau?
        # Cada corrida mais longa substituirá 'size', mas somente se o último membro da corrida
        # for maior que o número após ele, e o primeiro membro da corrida
        # é maior que o número anterior.
        # Como o contador está contando o comprimento da corrida, eu posso usá-lo para encontrar o início do plateau.
        if (cont>size) and (a[i+1]>a[i+2]) and (a[i-(cont-1)]>a[i-cont]):
            size=cont
            ind_inic=i-(cont-1) #encontra o começo do plateau.

    else:
        cont=0 #se não tem corrida, reseta o contador
    i+=1 #testa o proximo numero

print("Comprimento: "+str(size+1)+"\nLocalizacao:indice "+str(ind_inic))
