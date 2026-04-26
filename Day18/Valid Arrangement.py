# Global variable to store count of valid arrangements
count = 0
def solve(pos, n, used):
    global count  # use global count variable
    # If all positions are filled → valid arrangement
    if pos > n:
        count += 1  # increase count
        return
    # Try numbers from 1 to n
    for num in range(1, n + 1):
        # Check if number is not used AND valid condition
        if not used[num] and (num % pos == 0 or pos % num == 0):
            used[num] = True  # choose
            solve(pos + 1, n, used)  # go to next position
            used[num] = False  # undo (backtrack)
# ----------- MAIN -----------
n = 3
# Track used numbers (index 0 unused)
used = [False] * (n + 1)
solve(1, n, used)
print(count)  # Output: 3