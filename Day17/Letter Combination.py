def letter_combination(digits):
    if not digits:
        return []
    phone_map = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }
    res = []
    def backtrack(index, path):
        if index == len(digits):
            res.append(path)
            return
        for char in phone_map[digits[index]]:
            backtrack(index + 1, path + char)
    backtrack(0, '')
    return res
digits = input("Enter a string of digits (2-9): ")
print(f"Input: digits = {digits}")
print(f"Output: {letter_combination(digits)}")
