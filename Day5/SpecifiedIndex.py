arr = [10, 20, 30, 40, 50]

# Index to retrieve
index = int(input("Enter index: "))

# Check and print element
if index >= 0 and index < len(arr):
    print("Element:", arr[index])
else:
    print("Index out of range")