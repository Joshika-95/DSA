def generate_parentheses(n):
    result = []
    # Recursive function
    def backtrack(open_count, close_count, current):
        # Base case: if length is 2*n → add to result
        if len(current) == 2 * n:
            result.append(current)
            return
        # Add '(' if possible
        if open_count < n:
            backtrack(open_count + 1, close_count, current + "(")

        # Add ')' if valid
        if close_count < open_count:
            backtrack(open_count, close_count + 1, current + ")")
    # Start recursion
    backtrack(0, 0, "")
    return result
# Example
print(generate_parentheses(3))
