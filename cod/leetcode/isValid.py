class Solution(object):
    def isValid(self, nums):
        arr = []

        for i in range(len(nums)):
            if(len(arr)==0):
                arr.append(nums[i])
            elif(arr[len(arr)-1] =='(' and nums[i] ==')'):
                arr.pop()
            elif (arr[len(arr)-1] =='[' and nums[i] ==']'):
                arr.pop()
            elif (arr[len(arr)-1] =='{' and nums[i] =='}'):
                arr.pop()
            else:
                arr.append(nums[i])
        if(len(arr)==0):
            return True
        else:
            return False
if __name__ == '__main__':
    sl = Solution()
    
    print(sl.isValid("{[]}"))
        
            
        