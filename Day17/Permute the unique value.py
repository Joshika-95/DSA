def permuteUnique(nums):
    res = []

    def backtrack(path, remaining):
        if not remaining:
            if path not in res:   # avoid duplicates
                res.append(path)
            return
        
        for i in range(len(remaining)):
            backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])

    backtrack([], nums)
    return res

# Example
print(permuteUnique([1, 1, 2]))