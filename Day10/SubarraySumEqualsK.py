def subarraySum(nums, k):
    count = 0
    n = len(nums)

    for i in range(n):
        total = 0
        for j in range(i, n):
            total += nums[j]
            if total == k:
                count += 1

    return count
nums=[1,1,1]
k=2
print(subarraySum(nums,k))