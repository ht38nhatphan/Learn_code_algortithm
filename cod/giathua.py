import math
[n,k] = [int(x) for x in input().split()]
def giaithua(a,n):
    # gt = math.factorial(n)
    sum = a
    for i in range(2,n+1):
        sum = sum + (a**i/(math.factorial(i)))
    # g = str(sum)
    # g = g.index(

    return ("{:.2f}".format(sum))
    # return math.ceil(sum*100)/100
print(giaithua(n,k))

