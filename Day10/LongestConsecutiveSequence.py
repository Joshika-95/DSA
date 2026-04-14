def longestConsecutive(nums):
    s = set(nums)   # convert list to set
    longest = 0

    for x in s:
        # start only if x is the beginning of sequence
        if x - 1 not in s:
            count = 1
            while x + count in s:
                count += 1
            longest = max(longest, count)

    return longest
nums = [1,6,9,5,2]
print(longestConsecutive(nums))  # Output: 3