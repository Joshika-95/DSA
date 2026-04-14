def twoSum(nums, target):
    d = {}  # number -> index

    for i in range(len(nums)):
        num = nums[i]
        diff = target - num

        if diff in d:
            return [d[diff], i]

        d[num] = i

    return []


# Example
nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))  # Output: [0, 1]