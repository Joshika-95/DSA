# // Sample Testcases:

# // 1.s = "ab", goal = "abc"
# // o/p: false

# // 2.s = "aa", goal = "aa"  
# // o/p: true
s = input()
goal = input()

if len(s) != len(goal):
    print("false")
    exit()

if s == goal:
    count = [0] * 26
    for c in s:
        count[ord(c) - ord('a')] += 1
        if count[ord(c) - ord('a')] > 1:
            print("true")
            exit()
    print("false")
    exit()

    
first = -1
second = -1
for i in range(len(s)):
    if s[i] != goal[i]:
        if first == -1:
            first = i
        elif second == -1:
            second = i
        else:
            print("false")            
            exit()

if second != -1 and s[first] == goal[second] and s[second] == goal[first]:
    print("true")
else:
    print("false")
