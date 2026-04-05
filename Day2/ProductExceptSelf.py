def productExceptSelf(nums):
    n=len(nums)
    result=[0]*n
    for i in range(n):
        product=1
        for j in range(n):
            if i==j:
                product*=nums[j]
        result=product
        return result
nums=[1,2,3,4]
print(productExceptSelf(nums))