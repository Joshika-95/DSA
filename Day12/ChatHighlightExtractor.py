def extract_mentions(chat):
    res = []
    seen = set()
    i = 0

    while i < len(chat):
        if chat[i] == '@':
            i += 1
            word = ""

            while i < len(chat) and chat[i].isalnum():
                word += chat[i]
                i += 1

            if word and word not in seen:
                res.append(word)
                seen.add(word)
        else:
            i += 1

    return res

print(extract_mentions("hello @!abc @123 @validUser"))
