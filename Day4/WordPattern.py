# Write a program to check whethere a given pattern matches a string.
# Each character in the patter should map to a word in the string such that:
#    1.Each character maps to exactly one word
#    2.No two characters map to the same word

# Example 1:
# sample input 
# Enter pattern: abba 
# Enter string: dog cat cat dog
# sample output: True

# Example 2:
# sample input
# Enter pattern: abcd
# Enter string: Biryani Parotaa Noodles
# sample output: False

pattern = input("Enter pattern: ")
s = input("Enter string: ")

words = s.split()

if len(pattern) != len(words):
    print(False)
else:
    char_to_word = {}
    word_to_char = {}
    match = True

    for i in range(len(pattern)):
        ch = pattern[i]
        word = words[i]

        if ch in char_to_word:
            if char_to_word[ch] != word:
                match = False
                break
        else:
            char_to_word[ch] = word

        if word in word_to_char:
            if word_to_char[word] != ch:
                match = False
                break
        else:
            word_to_char[word] = ch

    print(match)