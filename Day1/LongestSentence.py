text="This is my day","Happy day","Good morning"
max_len=0
longest=" "
for string in text:
    count=0
    for char in string:
        count+=1
        if count > max_len:
            max_len=count
            longest=string
print(longest)
print(len(longest.split(" ")))