arr = ["red", "Green", "Blue", "Violet"]
# input range
start = int(input("Enter start index: "))
end = int(input("Enter end index: "))

# extract portion
if 0 <= start <= end < len(arr):
    result = arr[start:end+1]
    print(",".join(result))
else:
    print("Invalid index range")