# # Check power of 2
def is_perfect_square(n, i=1):
    if n < 0:
        return False
    if i * i == n:
        return True
    if i * i > n:
        return False
    return is_perfect_square(n, i + 1)
num = int(input("Enter number to check: "))
print(is_perfect_square(9))

# Find 2^n
def power_of_two(n):
    if n == 0:
        return 1
    return 2 * power_of_two(n - 1)

# Input
n = int(input("Enter power (n): "))
print(power_of_two(n))        # 2^n value

    
