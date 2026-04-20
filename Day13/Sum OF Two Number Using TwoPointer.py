def two_sum_sorted(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return (arr[left], arr[right]), (left, right)  # values, index
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return None, None


# Example
arr = [1, 2, 3, 4, 6]
target = 6

values, index = two_sum_sorted(arr, target)

print("Values:", values)
print("Index:", index)