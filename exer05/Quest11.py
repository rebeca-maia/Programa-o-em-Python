"""
Componha um programa que pega 3 argumentos da linha de comando m,n e p e produza um array m por n booleano onde cada elemento é ocupado
com probabilidade p. No jogo minesweeper, células ocupadas representam bombas e células vazias representam células seguras. Escreva o
array usando um asterisco para bombas e um ponto para células seguras. Então, substitua cada célula segura com o número de bombas vizihas
(em cima, embaixo, direita, esquerda ou diagonal) e escreva o resultado.
"""
m=int(input())
n=int(input())
p=float(input())

mine=[]

for i in range(m):
    row =[True]*n #True para desocupado, False para ocupado
    mine+=[row]


