def count_good_numbers(n):

    result = 1  # store final answer
    # Loop through each position
    for i in range(n):
        # Even index → 5 choices
        if i % 2 == 0:
            result *= 5
        # Odd index → 4 choices
        else:
            result *= 4
    return result
# Example
print(count_good_numbers(4))

# DRY RUN:
# index =0(even)
# result =1*5 =5
# index =1(odd)
# result = 5*4=20
# index=2(even)
# result=20*5=100
# index=3(odd)
# result =100*4=40
# index=4(false)
# exit result=400
