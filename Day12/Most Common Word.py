def mostCommonWord(paragraph, banned):
    banned = set(banned)
    count = {}

    words = paragraph.lower().split()

    for word in words:
        word = word.strip('.,!?')
        
        if word not in banned:
            count[word] = count.get(word, 0) + 1

    return max(count, key=count.get)


# Example 
paragraph = "Apple banana apple orange banana apple fruit"
banned = ["banana"]

print(mostCommonWord(paragraph, banned))