def sequentialDigits(low, high):
    res = []
    s = "123456789"
    
    for length in range(2, 10):  # length of number
        for i in range(0, 10 - length):
            num = int(s[i:i+length])
            
            if low <= num <= high:
                res.append(num)
    
    return res

# Example
print(sequentialDigits(100, 1000))