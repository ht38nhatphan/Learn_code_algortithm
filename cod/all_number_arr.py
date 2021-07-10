# Python program to print all
# the possible combinations
  
# Get all combination of [1, 2, 3]
# of length 3
from itertools import permutations
from itertools import product
coma = permutations([1, 2, 3],3)
for j in coma:
    print(str(j))

#get all number in arr
#of length 3
comb = product([1,2,3,4,5,5,6,7,3,2], repeat= 3)
print("-------------") 

for i in comb:
    print(str(i))