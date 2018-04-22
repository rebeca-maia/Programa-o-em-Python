from calendar import month

#Gerar o calendário de determinado mês
m=int(input("Informe o mes:")) #6-Junho 7-Julho
y=int(input("Informe o ano: "))


def calendario(m,y):
    if (m >=1 and m<=12) and (y>=1900 and y<=2100):
        cal = month(y, m)
        print(cal)
    else:
        print("Entrada invalida")


calendario(m,y)