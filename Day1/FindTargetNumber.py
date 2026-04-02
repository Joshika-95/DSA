arr=[2,5,4,3,2]
target=5
res=[]
for num in arr:
    bal=target-num
    if bal in res:
        print("Two numbers: ",num,bal)
    res.append(num)
