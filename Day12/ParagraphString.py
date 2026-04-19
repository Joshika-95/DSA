def most_common_word(paragraph, banned):
    words = paragraph.lower().split()
    freq = {}

    for word in words:
        if word not in banned:
            freq[word] = freq.get(word, 0) + 1

    max_word = ""
    max_count = 0

    for word in freq:
        if freq[word] > max_count:
            max_count = freq[word]
            max_word = word

    return max_word


# Sample input
paragraph = "Bob hit a ball the hit ball flew far after it was hit"
banned = ["hit"]

print(most_common_word(paragraph, banned))  # Output: ball