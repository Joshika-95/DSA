def containsNearbyDuplicate(nums, k):
    last_index = {}  # Dictionary to store last index of each number
    for i in range(len(nums)):
        num = nums[i]
        if num in last_index and i - last_index[num] <= k:
            return True
        last_index[num] = i  # Update last seen index
    return False

# Example
nums = [1,2,3,1]
k = 6
print(containsNearbyDuplicate(nums, k))  # Output: True