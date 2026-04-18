# User-defined functions
# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Cannot divide by zero"
#     return a / b


print("----Calculator----")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter your choice:")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: ")) 

# Switch-case using match
match choice:
    case '1':
        print("Result:", (num1+num2))
    case '2':
        print("Result:", (num1-num2))
    case '3':
        print("Result:", (num1*num2))
    case '4':
        if num2==0:
            print("Cannot divide by zero")
        else:
            print("Result:",(num1/num2))
    case '5':
        print("Invalid choice")