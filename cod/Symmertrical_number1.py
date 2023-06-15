from itertools import product
[n,k] = [int(x) for x in input().split()]
arr = []
for i in range(0,n):
    g = int(input())
    arr.append(g)
# get all number in arr of length b
def symmertrical(a,b):
    c = len(a)
    a = set(a)
    # print(a)
    j = len(a)
    if(c == j and b==1):
        return c*2
    elif(c != j and b==1):
        return c-1
    else:
        n = len(a) 
        if b == 2:
            return n
        else:
            g = n-1
            d = n + (g*n)
            return d
print(symmertrical(arr,k))


