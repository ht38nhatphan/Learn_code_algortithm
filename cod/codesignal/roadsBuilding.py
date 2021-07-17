import numpy as np
def roadsBuilding(cities, roads):
    arr1 = []

    matrick = np.zeros((cities,cities),dtype=int)
    for i in range(len(roads)):
        matrick[roads[i][0]][roads[i][1]] = 1
        matrick[roads[i][1]][roads[i][0]] = 1
    for i in range(cities):
        for j in range(cities):
            if matrick[i][j] ==0 and matrick[j][i] ==0 and j!=i:
                arr = []
                arr.append(i)
                arr.append(j)
                matrick[i][j] = 1
                matrick[j][i] = 1
                arr1.append(arr)
            j = j+1 
    return arr1
print(roadsBuilding(9,[[5,8], 
 [6,0], 
 [0,5], 
 [4,1], 
 [0,1], 
 [7,0], 
 [6,8], 
 [7,3], 
 [2,6], 
 [0,2], 
 [0,3], 
 [8,7], 
 [5,4], 
 [8,4], 
 [8,2], 
 [7,1], 
 [4,6], 
 [5,6], 
 [4,2], 
 [4,7], 
 [2,7], 
 [3,6], 
 [8,0], 
 [1,6], 
 [3,2], 
 [3,4], 
 [4,0], 
 [6,7], 
 [5,7]]))