from math import sqrt
def theSmallestRadius(n,x,y):
    lis = []
    k = len(x)
    for i in range(k):
        for j in range(i+1,k):
            lis.append(sqrt((x[j]-x[i])**2+(y[j]-y[i])**2))
    ans = round(max(lis)/2,3)
    return "{:.3f}".format(ans)

print(theSmallestRadius(3,[0,5,1],[0,0,1]))