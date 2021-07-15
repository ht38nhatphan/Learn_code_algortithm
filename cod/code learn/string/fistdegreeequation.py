def firstDegreeEquation(s):
    

    a = s[s.index("=")+1:]
    if(s.find("x/0")>=0): return "Math error"
    if(s.find("/")>0):
        if s.find("+")>=0:
            a = "("+s[s.find("=")+1:]+")"+"*"+s[s.find("/")+1:s.find("+")]
        elif s.find("-")>0:
            a = "("+s[s.find("=")+1:]+")"+"*"+s[s.find("/")+1:s.find("-")]
        else:
            a = "("+s[s.find("=")+1:]+")"+"*"+s[s.find("/")+1:s.find("=")]
        a = "-"+ a.replace("+","-")
        s = s[0:s.index("/")]+a
    else:
        a = "-"+ a.replace("+","-")
        s = s[0:s.index("=")]+a
    
    

    chot = 1000000000/2
    s2 = str(eval(s.replace("x","1000000000")))
    #print(len(s2))
    hs = []
    # if(s2.find(".")>0):
    #     s2 = s2[0:s2.find(".")]
    am = False
    if s2[0] == '-':
        am = True
        s2 = s2[1:]
    i = len(s2) - 1
    nho = False
    nho2 = False
    while i >= 0:
        if i >= 8:
            n = int(s2[i - 8: i + 1])
            if n <= chot:hs.append(n)
            else: hs.append(n - 1000000000);nho=True
        else :
            n = int(s2[0:i + 1])
            if n <= chot:hs.append(n)
            else: hs.append(n - 1000000000);nho=True
        i -= 9
        if nho2:
            nho2 = False
            hs[-1] += 1
        if nho: nho2 = True;nho = False
    if nho2: hs.append(1)
    if am:
        for i in range(len(hs)):
            hs[i] = -hs[i]
    res = ""
    a = 0
    for j in range(len(hs) - 1, -1, -1):
        if hs[j] == 0 :
            continue
        if hs[j] == 1 : pass
        elif hs[j] == -1 : res += "-"
        elif hs[j] > 0 : res += "+" + str(hs[j]) 
        else : res += str(hs[j])
        if j != 0 and (hs[j] == -1 or hs[j] == 1):
            if hs[j] == 1: res += "+x"
            else: res += "x"
        elif hs[j] != 0 and j != 0: res += "*x"
        elif (hs[j] == 1 or hs[j] == -1) and j == 0:
            if hs[j] == 1: res += "+1"
            else: res += "1"
        if j != 0 and j != 1:
            res += "^" + str(j)
    if res == "" : res = "0"
    if res[0] == '+' : res = res[1:]
    if(res.find("x")<0):
        return hs[0] ==0 and "Infinite Solution" or "No solution"
    elif(res.find("*")>0):
        if hs[1]>0:    
            n = hs[0]>0 and hs[0] or -hs[0]
            kk = hs[0] % hs[1] ==0 and str(round(n/hs[1])) or str(n)+'/'+str(hs[1])
            return kk
        elif hs[1]<0:
            c = hs[0]>0 and hs[0] or -hs[0]
            kk = hs[0] % hs[1] ==0 and str(round(c/hs[1])) or str(c)+'/'+str(hs[1])
            return kk
    elif res.find("x")>=0:
        return hs[1]>0 and str(-hs[0]) or str(hs[0])

    
print(firstDegreeEquation("x/0=4"))
