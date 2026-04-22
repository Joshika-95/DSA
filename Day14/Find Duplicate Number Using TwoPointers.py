def find_duplicate(nums):
    # Step 1: Find intersection point in cycle
    slow=fast=nums[0]
    while True:
        slow=nums[slow]
        fast=nums[nums[fast]]
        if(slow==fast):
            break
    # Step 2: Find entrance to the cycle (duplicate)
    slow=nums[0]
    while slow!=fast:
        slow=nums[slow]
        fast=nums[fast]
    return slow

nums=[1,3,4,2,2]
print(find_duplicate(nums))