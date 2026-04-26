def comb(k, n):
    res = []

    def bt(start, path):
        if len(path) == k:
            if sum(path) == n:
                res.append(path[:])
            return
        
        for i in range(start, 10):
            path.append(i)
            bt(i + 1, path)
            path.pop()

    bt(1, [])
    return res

# Example
print(comb(3, 9))