my_dict = {
    "name": "Sripriya",
    "age": 18,
    "city": "salem"
}
key = input("Enter the key to check: ")

if key in my_dict:
    print("The key exists in the dictionary.")
else:
    print("The key does not exist in the dictionary.")  
