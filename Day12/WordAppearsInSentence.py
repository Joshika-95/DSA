def count_word_frequency(sentence):
    # Step 1: Split sentence into words
    words = sentence.split()
    
    # Step 2: Create an empty dictionary
    frequency = {}
    
    # Step 3: Count each word
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    # Step 4: Print result
    for word, count in frequency.items():
        print(f"{word} → {count}")

# Input
sentence = "apple banana apple orange banana apple"

# Function call
count_word_frequency(sentence)