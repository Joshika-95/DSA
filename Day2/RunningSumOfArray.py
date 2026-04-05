def runningSum(nums):
    result=[]
    total=0
    for num in nums:
        total+=num
        result.append(total)
    result
nums=[1,2,3,4]
print(runningSum(nums))