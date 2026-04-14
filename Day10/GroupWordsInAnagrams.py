def group_anagrams(words):
    d = {}  # dictionary

    for word in words:
        key = ''.join(sorted(word))  # create key

        if key in d:
            d[key].append(word)
        else:
            d[key] = [word]

    return d.values()


# Example
words = ["eat", "tea", "ate", "tan", "nat", "bat"]

result = group_anagrams(words)

for group in result:
    print(list(group))