def topKFrequent(nums, k):
    freq = {}

    # count frequency
    for n in nums:
        freq[n] = freq.get(n, 0) + 1

    # sort by frequency (highest first)
    sorted_nums = sorted(freq, key=freq.get, reverse=True)

    return sorted_nums[:k]
nums = [1,1,1,2,2,3]
k = 2

print(topKFrequent(nums, k))  # Output: [1, 2]