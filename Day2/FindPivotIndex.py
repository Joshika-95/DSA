def pivotIndex(nums):
    for i in range(len(nums)):
        left_sum=0
        right_sum=0
        for j in range(i):
            left_sum+=nums[j]
            for i in range(i+1,len(nums)):
                right_sum+=nums[i]
            if left_sum==right_sum:
                return i
            return -1
nums=[1,7,3,6,5,6]
print(pivotIndex(nums))