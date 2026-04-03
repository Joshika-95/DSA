arr=[1,2,3,4]
prefix_sum=[]
current_sum=0
for num in arr:
    current_sum+=num
    prefix_sum.append(current_sum)
print(prefix_sum)