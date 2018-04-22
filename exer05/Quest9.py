from random import randrange

n=int(input())

a=[0]*n
prob=0
for i in range(1,n):
    a[i] = 1
    r=randrange(i,n)
    if i==r: continue
    elif a[r]==0:
        a[r]+=1
        prob+=1
    elif a[r]==1:
        continue

print(a)
print("%.2f"%(prob/n))