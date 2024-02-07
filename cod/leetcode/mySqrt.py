import math as m
class Solution(object):
    def findnumber(self, s):
        i,str= 0,""
        while(i<=len(s) and s[i]!='.'):
            str += s[i]
            i+=1
        
        return str
    def mySqrt(self, x):
        return (int(self.findnumber(str(m.sqrt(x)))))
        

if __name__ == '__main__':
    sl = Solution()
    
    print(sl.mySqrt(6))