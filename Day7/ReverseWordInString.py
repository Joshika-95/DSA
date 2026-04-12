s = input()
words = s.split(" ")
result = ""
for word in words:
    rev = ""
    for i in range(len(word) - 1, -1, -1):
        rev += word[i]
    result += rev + " "
print(result.strip())