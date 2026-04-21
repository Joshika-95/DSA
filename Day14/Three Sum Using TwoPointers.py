def three_sum(nums):
    nums.sort()
    res=[]
    for i in range (len(nums)):
        l,r=i+1,len(nums)-1
        while l<r:
            s=nums[i]+nums[l]+nums[r]
            if s==0:
                res.append([nums[i],nums[l],nums[r]])
                l+=1
                r-=1
            elif s<0:
                l+=1
            else :
                r-=1
    return res
nums=[-1,0,1,2,-1,-4]
print(three_sum(nums))
