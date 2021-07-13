def removeDuplicates(nums):
    set1=dict.fromkeys(nums)
    #print(set1)
    x=len(set1)
    #print("length of set is : ",x)
    for i,val in enumerate(set1):
        nums[i]=val
    #print(nums)
    return x
print(removeDuplicates([1,1,2]))