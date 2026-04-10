profit=[3,4,7,2,-3,1,4,2]
target=7
count=0
curr_sum=0
profit={0:1}
for num in profit:
    curr_sum+=num
    if (curr_sum-target) in profit:
        count+=profit[curr_sum-target]
        profit[curr_sum]=profit.get(curr_sum,0)+1
print(count)