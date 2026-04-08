string= input("Enter a string: ")
index = int(input("Enter index: "))

if index >= 0 and index < len(string):
    print("Character at index:", string[index])
else:
    print("Invalid index")