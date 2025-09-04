def count(n):
    c=0
    while n>0:
        r=n%10
        c+=1
        n//=10
    return c
num=int(input("Enter a number: "))
print("Number of digits in",num,"is:",count(num))