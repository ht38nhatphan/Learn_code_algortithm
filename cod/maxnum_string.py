import re   
n = str(input())

def getarr(strs):
    pattern = '\d+'
    g = re.findall(pattern,strs)
    g = list(map(int,g))
    return max(g)
print(getarr(n))
