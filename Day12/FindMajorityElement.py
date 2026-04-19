def majorityElement(nums):
    count = {}
    result = []
    n = len(nums)

    for num in nums:
        count[num] = count.get(num, 0) + 1

    for key in count:
        if count[key] > n // 3:
            result.append(key)

    return result


# Example
nums = [3, 2, 3, 2, 2, 1]
print(majorityElement(nums))