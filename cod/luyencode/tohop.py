# tổ hợp chập k của n
from math import factorial
[n,k] = [int(x) for x in input().split()]
h = int(factorial(n)/(factorial(k)*factorial(n-k)))
print (h)