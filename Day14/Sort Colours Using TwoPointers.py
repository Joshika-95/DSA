def sort_colors(nums):
    left = 0
    right = len(nums) - 1

    # Move all 2s to the end
    i = 0
    while i <= right:
        if nums[i] == 2:
            nums[i], nums[right] = nums[right], nums[i]
            right -= 1
        else:
            i += 1

    # Move all 0s to the beginning
    i = 0
    while i < len(nums) and i >= left:
        if nums[i] == 0:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
        i += 1

# Example
arr = [2, 0, 2, 1, 1, 0]
sort_colors(arr)
print(arr)  