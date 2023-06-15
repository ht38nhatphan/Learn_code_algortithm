import math
[a,n] = [int(x) for x in input().split()]
def primeGCD(a,b):
#  h=math.gcd(a,b)
#  return isPrime(h)
 return math.gcd(a,b)
print(primeGCD(a,n)