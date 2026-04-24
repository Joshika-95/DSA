# Two input arrays
arr1 = [1, 2, 5, 5, 6]
arr2 = [2, 5, 7, 6, 8]

# Convert first array to a set
set1 = set(arr1)

# Store common elements (duplicates between arrays)
result = set()

# Check elements of second array
for num in arr2:
    if num in set1:
        result.add(num)

print("Common elements:", result)
