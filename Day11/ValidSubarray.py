nums = [23, 2, 4, 6, 7]
k = 6

d = {}
s = 0

for i in range(len(nums)):
    s += nums[i]
    r = s % k

    if r == 0 and i > 0:
        print(nums[0:i+1])
        break

    if r in d:
        print(nums[d[r] + 1:i + 1])
        break
    else:
        d[r] = i