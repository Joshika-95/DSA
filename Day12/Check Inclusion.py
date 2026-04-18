def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    # frequency of s1
    d1 = {}
    for ch in s1:
        d1[ch] = d1.get(ch, 0) + 1

    window = len(s1)

    for i in range(len(s2) - window + 1):
        d2 = {}

        # frequency of current window in s2
        for ch in s2[i:i+window]:
            d2[ch] = d2.get(ch, 0) + 1

        if d1 == d2:
            return True

    return False


# Example
s1 = "ab"
s2 = "eidbaooo"

print(checkInclusion(s1, s2))