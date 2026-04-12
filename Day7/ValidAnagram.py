# Rule for angaram:
#     1. length should be equal
#     2. Same characters should be present in tow string variable(But in anyorder)
def isAnagram(a, b):
    return sorted(a) == sorted(b)
a = input("Enter first : ")
b = input("Enter second : ")
if isAnagram(a, b):
    print("Valid Anagram")
else:
    print("Not an Anagram")
