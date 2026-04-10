def countAndSay(n):
    result = "1"  # starting value
    for i in range(2, n + 1):
        next_seq = ""
        count = 1
        for j in range(len(result)):
            # if next char same
            if j < len(result) - 1 and result[j] == result[j + 1]:
                count += 1
            else:
                next_seq += str(count) + result[j]
                count = 1
        result = next_seq
    return result
print(countAndSay(5))