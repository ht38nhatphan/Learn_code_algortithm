n = int(input())
# mod = int(1e9)+7
def sohh(n):
    dem = 0
    for i in range(1,int(n/2)+1):
        if n%i==0:
            dem = dem+i
    if dem == n:
        return "YES"
    else:
        return "NO"
# def sinhso(m):
#     arr = []
#     for i in range(1,mod):
#         if sohh(i) == 'YES':
#             arr.append(i)
#     return arr
    
print(sohh(n))
