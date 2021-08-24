
[n,p] = [int(x) for x in input().split()]
if n==p:
    print (n-1)
elif p>n:
    print( 0)
else:
    result = 1
    m = n
    while n:
        temp = n%p
        result *= (temp+1)
        n /= p
    print (m+1-result)