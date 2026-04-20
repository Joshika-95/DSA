def sort_by_frequency(s):
    freq = {}

    # Count frequency
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    result = ""

    # Loop until dictionary is empty
    while freq:
        max_char = None
        max_count = 0

        # Find character with highest frequency
        for ch in freq:
            if freq[ch] > max_count:
                max_count = freq[ch]
                max_char = ch

        # Add to result
        result += max_char * max_count

        # Remove that character from dictionary
        del freq[max_char]

    return result

# Example
s = "bottle"
print(sort_by_frequency(s))  