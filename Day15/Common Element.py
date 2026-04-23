def no_common_elements(set1, set2):
    return len(set1.intersection(set2)) == 0

# Example
set1 = {1, 2, 3, 4}
set2 = {4, 5, 6, 7}

print(no_common_elements(set1, set2))