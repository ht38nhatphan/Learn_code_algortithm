from collections import OrderedDict

# def countAPI(calls):
#     r = OrderedDict()
#     for call in calls:
#         p, s, m = tuple(call.split('/')[1:])
#         try:
#             r[p][s][m] += 1
#         except KeyError as e:
#             e = e.args[0]
#             if str(e) == p:
#                 r[p] = OrderedDict()
#                 r[p][s] = OrderedDict()
#                 r[p][s][m] = 1
#             elif str(e) == s:
#                 r[p][s] = OrderedDict()
#                 r[p][s][m] = 1
#             else:
#                 r[p][s][m] = 1

#     return r

def countAPI(calls):
    x={}
    y={}
    a=[]
    b={}
    c={}
    for i in calls:
        k=i.split("/")
        if k[1] not in x:
            x[k[1]]={}
            y[k[1]]=0
            a+=[k[1]]
            b[k[1]]=[]
            c[k[1]]={}
        if k[2] not in x[k[1]]:
            x[k[1]][k[2]]={}
            y[k[1]+k[2]]=0
            b[k[1]]+=[k[2]]
            c[k[1]][k[2]]=[]
        if k[3] not in x[k[1]][k[2]]:
            x[k[1]][k[2]][k[3]]=0
            c[k[1]][k[2]]+=[k[3]]
        y[k[1]]+=1
        y[k[1]+k[2]]+=1
        x[k[1]][k[2]][k[3]]+=1
    z=[]
    for i in a:
        z.append("--"+i+" ("+str(y[i])+")")
        for j in b[i]:
            z.append("----"+j+" ("+str(y[i+j])+")")
            for k in c[i][j]:
                z.append("------"+k+" ("+str(x[i][j][k])+")")
    return z

calls=["/project1/subproject1/method1", 
 "/project2/subproject1/method1", 
 "/project1/subproject1/method1", 
 "/project1/subproject2/method1", 
 "/project1/subproject1/method2", 
 "/project1/subproject2/method1", 
 "/project2/subproject1/method1", 
 "/project1/subproject2/method1"]
print(countAPI(calls))
