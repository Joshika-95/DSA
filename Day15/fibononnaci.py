def fib(n):
    if n == 0:  # base case
        return 0
    if n == 1:  # base case
        return 1
    return fib(n-1) + fib(n-2)  # recursive call
print(fib(5))  # output: 5