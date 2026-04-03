arr=[1,2,2,4,5,5,1]
unique=[]
for num in arr:
    if num not in unique:
        unique.append(num)
print(unique)