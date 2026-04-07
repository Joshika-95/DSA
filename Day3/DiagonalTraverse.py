def diagonal_traverse(matrix):
    if not matrix:
        return []

    rows, cols = len(matrix), len(matrix[0])
    result = []
    r = c = 0
    up = True  # Direction flag: True = up-right, False = down-left

    for _ in range(rows * cols):
        result.append(matrix[r][c])

        if up:
            if c == cols - 1:  # Hit right boundary
                r += 1
                up = False
            elif r == 0:        # Hit top boundary
                c += 1
                up = False
            else:
                r -= 1
                c += 1
        else:
            if r == rows - 1:  # Hit bottom boundary
                c += 1
                up = True
            elif c == 0:        # Hit left boundary
                r += 1
                up = True
            else:
                r += 1
                c -= 1

    return result

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(diagonal_traverse(matrix))
