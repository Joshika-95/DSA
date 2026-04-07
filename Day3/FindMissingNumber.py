def findMissingNumber(nums):
    max_val=max(nums)
    present=[False]*(max_val+1)
    for num in nums:
        present[num]=True
    result=[]
    for i in range(1,max_val+1):
        if not present[i]:
            result.append(i)
    return result
nums=[1,4,3,7,2]
print(findMissingNumber(nums))