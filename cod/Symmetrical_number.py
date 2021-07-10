from itertools import product
[n,k] = [int(x) for x in input().split()]
arr = []
for i in range(0,n):
    g = int(input())
    arr.append(g)
def is_symmetrical(number):
    n = len(number)
    if n == 2:
        return number[0] == number[1]
    elif n % 2 == 0:
        d = (int)(n/2)
        return sum(number[0:d]) == sum(number[(d)-1:])
    else:
        n = n + 1
        d = (int)(n/2)
        return sum(number[0:d]) == sum(number[(d)-1:])
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
        comb = product(a, repeat= b)
        g =list(comb)
        dem = 0
        # for i in range(0, len(g)):
        #     h = str(g[i])
        #     h = h[1:len(h)-1]
        #     h = h.replace(", ","")
        #     # print(h)
        #     if(is_symmetrical(h)):
        #         dem = dem +1 
        for i in range(0, len(g)):
            h = str(g[i])
            h = h[1:len(h)-1]
            h = h.replace(", ","")
            h = list(h)
            #join string to int
            h = list(map(int,h))
            # k = h[1:]
            # j = sum(k)
            # g[i] = h
            # # print(h)
            if(is_symmetrical(h)):
                 dem = dem +1
        return dem
print(symmertrical(arr,k))


