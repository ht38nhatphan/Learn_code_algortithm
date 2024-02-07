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
# #tham khảo       
# import math 
# class Solution(object):
#     def mySqrt(self, x):
#         low = 1
#         high = x

#         if x == 0 or x == 1:
#             return x
        
#         while low <= high:
#             mid = (low + high) // 2
#             if mid * mid == x:
#                 return mid
#             elif mid * mid < x:
#                 low = mid + 1
#             else:
#                 high = mid - 1
#         return high
        


if __name__ == '__main__':
    sl = Solution()
    
    print(sl.mySqrt(6))