def sum_range(nums,left,right):
    total=0
    for i in range(left,right+1):
        total+=nums[i]
    return total
nums=[2,4,5,7,8]
print(sum_range(nums,1,3))