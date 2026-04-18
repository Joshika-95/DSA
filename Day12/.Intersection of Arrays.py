def intersection(nums1, nums2):
    d = {}
    res = []

    for num in nums1:
        d[num] = 1

    for num in nums2:
        if num in d:
            res.append(num)
            d.pop(num)  # avoid duplicates

    return res
nums1 = [1, 2, 2, 3]
nums2 = [2, 2, 3, 4]

print(intersection(nums1, nums2))
