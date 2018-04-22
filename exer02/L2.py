# Types - Creative Exercises
# Questao 1

import random
import math
from sympy import *


print("Calculo do juro composto")

p = float(input("Capital inicial: "))
r = float(input("Taxa de juros anual: "))
t = float(input("Quantidade de anos: "))


m = p**(r*t)

print("Montante: %.2f" %m)

#Questao 2
print("Vento Frio")

t = float(input("Informe a temperatura em Fahrnheit, desde que seu valor absoluto não seja maior que 50: "))
v = float(input("Velocidade do vento em milhas por hora desde que o valor esteja entre 3 e 120: "))

w = (35.74+(0.6215*t))+((0.4275*t)-35.75)*(v**0.16)

print("Resultado: %.2f" %w)

#Questao 3
print("Convertendo coordenadas cartesianas em coodernadas polares")

x=float(input("Informe o valor de x: "))
y=float(input("Informe o valor de y: "))

#a distancia entre o ponto e a origem
r = math.sqrt((x*x)+(y*y))

#angulo formado por este segmento de reta que une esse ponto à origem e o eixo x
tetha = math.atan2(y,x)

print("Resultado:  "+str(r),(tetha))

# Questão 4


print("Numeros aleatorios de Gauss")

u = random.uniform(0,1)
v = random.uniform(0,1)

z = (limit(-2, u, 1) ** (1 / 2)) * sin(2 * math.pi * v)

print("Resultado: "+str(z))

#Questão 5
#Componha um programa que tome três floats x, y e z como argumentos de linha de comando e
# escreva True se os valores forem estritamente ascendentes ou descendentes (x <y <z ou x> y> z) e False caso contrário.
x=float(input("Digite um numero: "))
y=float(input("Digite outro numero: "))
z=float(input("Digite outro numero: "))

print(x<y<z or x>y>z)

#Questao 6 - Descobrir o dia da semana

d = int(input("Digite o dia: "))
m = int(input("Digite o mes: "))
y = int(input("Digite o ano: "))

y0 = y - (14 - m) // 12
x = y0 + y0//4 - y0//100 + y0 // 400
m0 = m + 12 * ((14 - m) // 12) - 2
d0 = (d + x + (31*m0) // 12) % 7

print("Resultado: %i"%d0)

#Questao 7
#Componha um programa que escreva cinco floats aleatórios uniformes entre 0 e 1,
#seu valor médio e seu valor mínimo e máximo. Use as funções incorporadas max () e min ().
a =(random.uniform(0,1))
print("%.f" %math.ceil(a))
print("%.f" %math.floor(a))
print("%.2f" %a)

b = (random.uniform(0,1))
print("%.2f" %b)

c = (random.uniform(0,1))
print("%.2f" %c)

d = (random.uniform(0,1))
print("%.2f" %d)

e = (random.uniform(0,1))
print("%.2f" %e)

#Questao 8 - Projeção de Mercator
phi=float(input("Digite a latitude: "))
lamb= float(input("Digite a longitude: "))
lambInic= float(input("A longitude do ponto no centro do mapa: "))

x=lamb-lambInic
y=1/2*limit((1+math.sin(phi))/(1-math.sin(phi)),x,1)
print("Latitude em coordenadas retangulares: "+str(x))
print("Longitude: "+str(x))

#Questão 9 - Converter formato RGB para CYMK

#cada variável recebe valores entre 0 e 255
r=float(input("Primeiro valor: "))
g=float(input("Segundo valor: "))
b=float(input("Terceiro valor: "))

w=max((r/255),(b/255),(g/255))

c = (math.fabs((w-r)/255))/w
m = (math.fabs((w-g)/255))/w
y = (math.fabs((w-b)/255))/w
k = math.fabs(1-w)
# Os valores estão na seguinte ordem: ciano, magenta, amarelo, preto
print("Valores: "+str(c),(m),(y),(k))

#Questao 10 - Distância de grande circulo
#O usuário passa as coordenadas em graus, e depois converte-se para radianos porque os métodos matemáticos nativos do phyton só
#lidam com radianos
x1 = math.radians(float(input("Digite a latitude: ")))
y1 = math.radians(float(input("Digite a longitude: ")))
x2 = math.radians(float(input("Digite a latitude: ")))
y2 = math.radians(float(input("Digite a longitude:")))

#depois converte-se novamente para graus e em seguida para milhas náuticas
d = 60 * math.degrees(math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2)))

print("%.2f" %d)

#usando a formula haversine para dá maior precisão
#os valores, em radianos, são convertidos para milhas náuticas
a = 60*math.sin((x2-x1)/2)*math.sin((x2-x1)/2) + math.cos(x1) * math.cos(x2) * math.sin((y2-y1)/2)*math.sin((y2-y1)/2)

print("%.2f" %a)


#Questão 11
#Compor um programa que aceita tres inteiros
# da linha de comando e os exibe em ordem ascendente.
a=int(input("Digite um numero: "))
b=int(input("Digite outro numero: "))
c=int(input("Digite outro numero: "))

x=max(a,b,c)
y=min(a,b,c)

if (c != x) and (c!=y):
    print("Ordem ascendente: "+str(y),(c),(x))
if (b!= x) and (b!=y):
    print("Ordem ascendente: "+str(y),(b),(x))
if(a !=x) and (a!=y):
    print("Ordem ascendente: "+str(y),(a),(x))


#Questão 12 - Desenhando as curvas do dragão

x0='F'
y0='F'
x1=x0+'L'+y0
y1=x0+'R'+y0
x2=x1+'L'+y1
y2=x1+'R'+y1
x3=x2+'L'+y2
y3=x2+'R'+y2
x4=x3+'L'+y3
y4=x3+'R'+y3
x5=x4+'L'+y4
print(x0)
print(x1)
print(x2)
print(x3)
print(x4)
print(x5)
