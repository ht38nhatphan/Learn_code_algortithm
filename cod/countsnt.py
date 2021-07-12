
# import sympy
# def get_primes(b,n):
#   m = n+1
# #   numbers = [True for i in range(m)]
# #   EDIT: faster
#   numbers = [True] * m 
#   for i in range(2, int(n**0.5 + 1)):
#     if numbers[i]:
#       for j in range(i*i, m, i):
#         numbers[j] = False
#   primes = []
#   for i in range(b, m):
#     if numbers[i]:
#       primes.append(i)
#   return primes
# # def snt(n):
# #     if(n<2): return False
# #     for i in range(2,int(math.sqrt(n))+1):
# #         if n % i ==0:
# #             return False
# #     return True
# def countsnt():
#     asd =[]
#     for i in arrs:
#         arrsave = get_primes(i[0],i[1])
#         asd.append(len(arrsave))
#     return asd
# # for i in arrs:
# #     print(i[0])
# # print(arrs[0][1])
# for i in countsnt(): 
#     print(i)
# # print(sieve(3))


# Python3 program to answer queries for
# count of primes in given range.
MAX = 10000000
 
# prefix[i] is going to
# store count of primes
# till i (including i).
prefix =[0]*(MAX + 1)
 
def buildPrefix():
     
    # Create a boolean array value in
    # prime[i] will "prime[0..n]". A
    # finally be false if i is Not a
    # prime, else true.
    prime = [1]*(MAX + 1)
 
    p = 2
    while(p * p <= MAX):
 
        # If prime[p] is not changed,
        # then it is a prime
        if (prime[p] == 1):
 
            # Update all multiples of p
            i = p * 2
            while(i <= MAX):
                prime[i] = 0
                i += p
        p+=1
 
    # Build prefix array
    # prefix[0] = prefix[1] = 0;
    for p in range(2,MAX+1):
        prefix[p] = prefix[p - 1]
        if (prime[p]==1):
            prefix[p]+=1
 
# Returns count of primes
# in range from L to
# R (both inclusive).
def query(L, R):
    return prefix[R]-prefix[L - 1]
#cách 2
# lower=int(input("lower value:"))          #let it be 30
# upper=int(input("upper value:"))          #let it be 60
# l=list(sympy.primerange(lower,upper+1))   #[31,37,41,43,47,53,59]
# z=len(l)
# print(z)
# Driver code
if __name__=='__main__':
    asd = []
    t = int(input())
    buildPrefix()
    for i in range(0,t):
        [l,r] = [int(x) for x in input().split()]
        asd.append(query(l,r))
    for i in asd: 
        print(i)
   
 
# This code is contributed by mits.