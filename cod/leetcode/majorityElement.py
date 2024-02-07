class Solution(object):
    def majorityElement(self, nums):
        dirs = {}
        numsmax,value = 1,nums[0]
        for i in range(len(nums)):
            
            if(dirs.get(nums[i])==None):
                dirs[nums[i]] = 1
            else:
                dirs[nums[i]] += 1
                # print(dirs[nums[i]])
                print(dirs[nums[i]])
                if(dirs[nums[i]]>numsmax):
                    numsmax = dirs[nums[i]]
                    value = nums[i]
        # max_key = max(dirs, key=lambda k: dirs[k])
        return value
if __name__ == '__main__':
    sl = Solution()
    
    print(sl.majorityElement([6,5,5]))