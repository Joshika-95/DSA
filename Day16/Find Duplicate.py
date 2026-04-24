arr1={4,5,6,7}
arr2={7,4,8,9}
unique=[]
for num in arr1:
    for nums in arr2:
        if num==nums:
            unique.append(num)
print("Duplicate: ",unique)
