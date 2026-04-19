def find_duplicates(arr):
    count = {}
    duplicates = []

    for num in arr:
        count[num] = count.get(num, 0) + 1

    for key, value in count.items():
        if value > 1:
            duplicates.append(key)

    return duplicates

# Example usage
arr = [10,15,83,95,10,83,100]
print(find_duplicates(arr))