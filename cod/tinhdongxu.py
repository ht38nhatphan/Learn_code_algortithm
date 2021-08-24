def change(a,b):
    if a==0: return 1
    if a<0 or len(b)==0: return 0
    # print(change(a-b[-1],b))
    return change(a-b[-1],b)+change(a,b[:-1])
'''bài toám tìm cách tính đồng xu'''
res={}
def g(a,b,c):
        if a==0: return 1
        if a<0 or len(b)==0: return 0
        if (a,c) not in res: res[(a,c)]=g(a-b[-1],b,c)+g(a,b[:-1],c-1)
        return res[(a,c)]
def h(a,b):
    # def g(a,b,c):
    #     if a==0: return 1
    #     if a<0 or len(b)==0: return 0
    #     if (a,c) not in res: res[(a,c)]=g(a-b[-1],b,c)+g(a,b[:-1],c-1)
    #     return res[(a,c)]
    return g(a,b,len(b)-1)

print(h(100,[5,2,1]))
print(res)