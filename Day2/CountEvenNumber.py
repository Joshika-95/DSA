def findNumbers(nums):
    count=0
    for num in nums:
        digit=len(str(num))
        if digit % 2==0:
            count+=1
        return count
nums=[12,345,2,6,7896]
print(findNumbers(nums))
