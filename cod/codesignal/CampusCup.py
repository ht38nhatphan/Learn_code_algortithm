# def campusCup(emails):
#     arr = []
#     arr1 = []
#     arr2 = []
#     arr3 = []
#     ik = 0
#     for i in emails:
#         if i.find("@")> 0:
#             g = df(arr,i[i.index("@")+1:])
#             if g>=0:
#                 if len(arr1)>0:
#                     c = g
#                     arr1[c] = arr1[c] + 20
                    
#             if g==-1 :
#                 arr.append(i[i.index("@")+1:])
#                 # arr3.append(i[i.index("@")+1:])
#                 arr1.append(20)
#             ik= ik + 1
#     for i in range(len(arr1)):
        
#         if arr1[i] >=100 and arr1[i]<200:
#             arr2.append(3)
#         elif arr1[i]<100:
#             arr2.append(0)
#         elif arr1[i]>=200 and arr1[i]<300:
#             arr2.append(8)
#         elif arr1[i]>=300 and arr1[i]<500:
#             arr2.append(15)
#         else:
#             arr2.append(25)
#     for i in range(len(arr1)-1):
#         for j in range(i+1,len(arr1)):
#             tmp = 0
#             if arr2[i] < arr2[j] and arr2[i]!=0 and arr2[j]!=0:
#                 tmp = arr[i]
#                 arr[i] = arr[j]
#                 arr[j] = tmp
#             elif arr2[i] == arr2[j] and arr1[i] > arr1[j] and arr2[i]!=0:
#                 tmp = arr[i]
#                 arr[i] = arr[j]
#                 arr[j] = tmp
#             elif arr1[i] < arr1[j] and arr2[i] ==0 and arr2[i]==0:
#                 tmp = arr[i]
#                 arr[i] = arr[j]
#                 arr[j] = tmp
#             elif arr2[i] == 0 and arr2[j]!=0:
#                 tmp = arr[i]
#                 arr[i] = arr[j]
#                 arr[j] = tmp

#     return arr

# # 3 4 2 1 5
# # 3   
# # 1 4 

# def df(arr,s):
#     for i in range(0,len(arr)):
#         if str(arr[i]).count(s)>0:
#             return i
#     return -1
def campusCup(e):
    d = {}
    for s in e:
        _, m = s.split("@")
        d[m] = d.get(m, 0) + 20
    return [a for a, _ in sorted(d.items(), key = lambda a: (-[0, 3, 8, 15, 15, 25][a[1]//100], a[0]))]
s = ["a@rain.ifmo.ru", 
 "b@rain.ifmo.ru", 
 "c@rain.ifmo.ru", 
 "d@rain.ifmo.ru", 
 "e@rain.ifmo.ru",  
 "a@mit.edu.ru", 
 "b@mit.edu.ru", 
 "c@mit.edu.ru",  
 "o@mit.edu.ru"]
g =list(set(s))
print(campusCup(s))
# code py 
# h = {}
# for k in re.findall("@(.*?)'",`vars()`):
#     h[k] = h.get(k,0) + 1
# return sorted(h, key=lambda k: [-(h[k]//5)+(h[k]>19),k])