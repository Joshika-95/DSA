text = "code"
word = "od"
answer = -1
# Loop through all possible starting positions
for i in range(len(text)):
    # Check if enough characters are left
    if i + len(word) <= len(text):
        part = text[i:i + len(word)]
        if part == word:
            answer = i
            break
print("Answer =", answer)