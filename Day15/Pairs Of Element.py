def find_pairs(nums, target):
    pairs = []
    
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.append((nums[i], nums[j]))
    
    return pairs

# Input
nums = list(range(10, 21))  # 10 to 20
target = 35

print(find_pairs(nums, target))