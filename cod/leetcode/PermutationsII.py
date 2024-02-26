class Solution(object):
    def permuteUnique(self, nums):
        def backtrack(start):
            if start == len(nums) - 1:
                result.append(list(nums))
                return
            setarr = set()
            for i in range(start, len(nums)):
                if nums[i] in setarr:
                    continue
                setarr.add(nums[i])
                nums[start], nums[i] = nums[i], nums[start]
                backtrack(start + 1)
                nums[start], nums[i] = nums[i], nums[start]

        result = []
        backtrack(0)
        return result
        
sl = Solution()
print(sl.permuteUnique([1,2,1]))