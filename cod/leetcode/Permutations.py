class Solution(object):
    def permute(self, nums):
        def backtrack(start):
            if start == len(nums) - 1:
                result.append(list(nums))
                return
            for i in range(start, len(nums)):
                nums[start], nums[i] = nums[i], nums[start]
                print( nums)
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        backtrack(0)
        return result
sl = Solution()
result = sl.permute([1,2,3])
print(result)
