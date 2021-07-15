import time
import math
#nhanh hơn
def get_primes(n):
  m = n+1
  #numbers = [True for i in range(m)]
  numbers = [True] * m #EDIT: faster
  for i in range(2, int(n**0.5 + 1)):
    if numbers[i]:
      for j in range(i*i, m, i):
        numbers[j] = False
  primes = []
  for i in range( m):
    if numbers[i]:
      primes.append(i)
  return primes
#cham hơn
def sieve(n):
    primes = [True]*(n+1)
    primes[0] = False
    primes[1] = False
    for i in range(2,int(math.sqrt(n+1))+1):
            j = i*i
            while j < n+1:
                    primes[j] = False
                    j = j+i
    return [x for x in range(n+1) if primes[x] == True]
# start = time.time()
# primes = get_primes(2,15)
# print(time.time() - start)
print(get_primes(15))
