from math import cos
#Pico de Fourier
n=int(input("Informe o algorismo: "))
def fourier(n):
    t=-10
    i=1
    sum=0
    while t<=10:
        sum+=cos(i*t)
        t+=1
        i+=1
    result=sum/n
    return result

if __name__=='__main__':
    a=fourier(n)
    print(a)