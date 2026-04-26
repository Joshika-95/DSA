def solve(index,nums,current,result):
    # Add current subset
    result.append(current[:])
    # Loop through remaining elements
    for i in range(index,len(nums)):
        current.append(nums[i])   
        solve(i+1,nums,current,result)
        current.pop()
nums=[1,2,3]
result=[]
solve(0,nums,[],result)
print(result)