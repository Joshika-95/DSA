def maximumWealth(account):
    max_wealth=0
    for customer in account:
        total=0
        for money in customer:
            total+=money
            if total> max_wealth:
                max_wealth=total
    return max_wealth
account=[
    [1,5],
    [7,3],
    [3,5]
]
print(maximumWealth(account))