class Solution(object):
    def singleNumber(self, nums):
        if(len(nums)==1):
            return nums[0]
        nums.sort()
        i = 0
        while(i<len(nums)):
            if(i+1<len(nums) and nums[i]!=nums[i+1]):
                return nums[i]
            elif(i+1==len(nums)):
                return nums[i]
            else:
                i += 2
        
        


sl = Solution()
s = sl.singleNumber([4,1,2,1,2])
print(s)