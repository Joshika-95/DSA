def subarraySum(nums,k):
    count=0
    for i in range(len(count)):
        total=0
        for j in range(j,len(nums)):
            total+=nums[j]
            if total==k:
                count+=1
    return count
nums=[1,1,1]
k=2
print(subarraySum(nums,k))