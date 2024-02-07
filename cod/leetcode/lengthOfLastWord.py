class Solution(object):     
    def lengthOfLastWord(self, s):
        s = s.strip()
        i,j = len(s)-1,0
        while(i>=0 and s[i]!=' '):
            j+=1
            i=i-1
        return j
        
        

if __name__ == '__main__':
    sl = Solution()
    
    print(sl.lengthOfLastWord("1"))