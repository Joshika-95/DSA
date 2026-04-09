# Write a program to reverse only the vowels in a given string.
# The program should modify the string such that:
#     1.Only the vowels(a,e,i,o,u)are reversed
#     2.All other characters remain in their original positions.

# Example 1:
# sample input: "hello"
# sample output: holle

# Example 2:
# sample input: "Priya"
# sample output: prayi

s = input("Enter a string: ")
vowels = "aeiouAEIOU"
v = []

# Store all vowels
for ch in s:
    if ch in vowels:
        v.append(ch)

# Reverse vowels
v = v[::-1]
# Empty string to build the final result
result = ""  
i = 0

# Replace vowels in string
for ch in s:
    if ch in vowels:
        result += v[i]
        i += 1
    else:
        result += ch

print("Output:", result)
