def sum(n):
    s=0
    i=1
    while i<=n:
        s+=i
        i+=1
    return s
num=int(input("Enter a number: "))
print("Sum of first",num,"natural numbers is:",sum(num))