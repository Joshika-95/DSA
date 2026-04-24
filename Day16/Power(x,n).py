def pow(x,n):
    if n==0:
        return 1
    else:
        return x*pow(x,n-1)
    
x=int(input("Enter the x value: "))
n=int(input("Enter the n value: "))

res=pow(x,n)

print(res)
