class Solution(object):
    def getPermutation(self, n, k):
        arr = self.genarate_number_arr(n)
        string = self.permute(arr, k)
        
        return self.convert_to_string(string)

    def permute(self, nums,k):
        def dfs(nums, path, output):
            if(len(output)==k):
                return
            if not nums:
                return output.append(path)
            
            for i in range(len(nums)):
                dfs(nums[:i]+nums[i+1:], path + [nums[i]], output)
        output = []
        dfs(nums, [], output)
        return output[k-1]

    def genarate_number_arr(self,num):
        arr = []
        for i in range(num):
            arr.append(i+1)
        return arr
    def convert_to_string(self,numbers):
        result_string = "".join(map(str, numbers))
        return result_string
sl = Solution()
result = sl.getPermutation(3,5)
print(result)