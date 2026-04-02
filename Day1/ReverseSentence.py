name=str(input())
rev=name[::-1]
for i in range(len(rev)):
    for j in range(i+1):
        print(rev[j],end=" ")
    print()