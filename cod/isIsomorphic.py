def isIsomorphic(s, t):
    if(len(s) ==1):
        return True
    for i in range(len(s)-1):
        if(s.count(s[i]) != t.count(t[i])):
            return False
        elif s[i] != s[i+1]:
            if t[i] == t[i+1]:
                return False
        elif s[i] == s[i+1]:
            if t[i] != t[i+1]:
                return False
    return True
    

print(isIsomorphic("bad","bab"))