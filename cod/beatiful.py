[a,b,k] = [int(x) for x in input().split()]
def beautiful(l):
    g = str(l)
    g = int(g[::-1])
    dem=0
    c = l-g
    if c<0:
        if -c%k==0 and c<0:
            return True      
    elif c>=0:
        if c%k==0 and c>=0:
            return True

    return False
def so():
    dem=0
    for i in range(a,b+1):
        if(beautiful(i)):
            dem+=1
    return dem

print(so())