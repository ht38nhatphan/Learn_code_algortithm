#tạo ma trận 
import numpy as np
import sys
[m,n] = [int(x) for x in input().split()]
matrick = np.zeros((m,m),dtype=int)

for i in range(0,m):
    [q,w,e] = [int(x) for x in input().split()]
    matrick[q-1][w-1] = e
    
print(matrick)
# matrick = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
#         [4, 0, 8, 0, 0, 0, 0, 11, 0],
#         [0, 8, 0, 7, 0, 4, 0, 0, 2],
#         [0, 0, 7, 0, 9, 14, 0, 0, 0],
#         [0, 0, 0, 9, 0, 10, 0, 0, 0],
#         [0, 0, 4, 14, 10, 0, 2, 0, 0],
#         [0, 0, 0, 0, 0, 2, 0, 1, 6],
#         [8, 11, 0, 0, 0, 0, 1, 0, 7],
#         [0, 0, 2, 0, 0, 0, 6, 7, 0]
#         ]
# [
#     [0,4,3,0,0,0,0,0],
#     [4,0,2,5,0,0,0,0],
#     [3,2,0,0,7,0,0,0],
#     [0,5,0,0,3,5,2,0],
#     [0,0,7,3,0,0,5,0],
#     [0,0,0,5,0,0,1,7],
#     [0,0,0,2,5,0,1,4],
#     [0,0,0,0,0,7,4,0]
# ]

#chuyển mảng thành ma trận dạng arr
A = np.array(matrick)
# print(len(A[0]))

#độ dài của mảng
length = len(A[0])


#tao ma trận chứa các đỉnh đi qua
trig = A
for i in range(0,length):
    for j in range(0,length):
        if(A[i][j]>0):
            trig[i][j] = 1
#tạo mảng với có các phần tử là số maxint
mang = np.zeros(shape=(length), dtype=int)+ sys.maxsize
#check mang rong
mangrong = np.zeros(shape=(length), dtype=int)
# np.where(trig>0,trig+10,trig)
# tạo mảng có length phần tử =0
# np.zeros(shape=(length,length), dtype=int)
# print(trig[0])

#tạo mảng lưu các đỉnh đã đi
luuding = np.zeros(shape=(length), dtype=int)+1
def chonding(n,d):
    #duyet mang lay do dai của đỉnh để đi
    for i in range(0,length):
        #neu dinh n đến đỉnh i =1 
        if trig[n][i] == 1:
            #với đinh đầu = 0 và mang[i]=max thì mang[i] = matrick[n][i]
            if n==d and mang[i]== sys.maxsize:
                mang[i] = matrick[n][i]
                #xoa các đỉnh đã đi
                matrick[n][i] = 0
                matrick[i][n] = 0
                trig[n][i] = 0
                trig[i][n] = 0
            #với đỉnh đầu khác = 0 và mang[n]+matrick[n][i]< mang[i] kiem tra neu dinh di bé hon thi lấy dộ dài lưu vào mảng
            if n!=d and mang[n]+matrick[n][i]< mang[i]:
                mang[i] = mang[n]+matrick[n][i]
                #xoá các đỉnh đã đi
                matrick[n][i] = 0
                matrick[i][n] = 0
                trig[n][i] = 0
                trig[i][n] = 0
            #lưu các đỉnh đã đi
            luuding[n]=0
#chon dinh khi di
def check1():
    tam = -1
    #cheack các đỉnh đã đi qua không đi lại 
    for i in range(0,len(luuding)):
        if luuding[i]!=0 :
            #chọn đỉnh đầu tiên khi tìm thấy
            tam = i
            break
    return tam
#duyệt phần tử trong mảng nếu bé hơn thì chọn đỉnh đó để đi
def check():
    tam = check1()
    if tam ==-1:
        return -1
    #cheack các đỉnh đã đi qua và không đi lại
    for i in range(0,len(luuding)):
        if luuding[i]!=0 and i!=tam and mang[tam] >mang[i]:
            tam = i
    return tam

def dijktra(d):
    chonding(d,d)
    while(True):
        #kiểm tra nếu không còn đỉnh nào để đi thì dừng lại
        a = check()
        if(a==-1):
            break
        for i in range(0,length):
            #kiểm tra nếu mảng rông thì dừng
            if np.array_equal(mangrong ,np.array(matrick[0])):
                return
        chonding(a,d)

#main
# print("Nhập đỉnh muốn đi: ")
# dinh = int(input())
dijktra(1)
mang[1]=0
i=0
#in mang
for distance in mang:
    print("Distance of ", chr(ord('a') + i)," from source vertex: ", distance)
    i = i + 1
    
