def binomial(n,k):
    #total=0
    if(n==0) or (k<0):
        return 1.0
    total=1
    total += (binomial(n - 1, k) + binomial(n - 1, k - 1)) / 2.0
    return total

p=binomial(4,3)
print(p)
