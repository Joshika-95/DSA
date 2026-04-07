arr=[1,4,4,7,2]
duplicate=-1
for i in range(len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]==arr[j]):
            duplicate=arr[i]
print(duplicate)