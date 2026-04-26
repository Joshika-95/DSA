def decode(s, i=0):
    if i == len(s):
        return 1
    
    if s[i] == '0':
        return 0
    
    # take one digit
    count = decode(s, i + 1)
    
    # take two digits using your condition
    if i + 1 < len(s):
        if s[i] == '1' or (s[i] == '2' and s[i+1] <= '6'):
            count += decode(s, i + 2)
    
    return count


# example
print(decode("22222226")) 