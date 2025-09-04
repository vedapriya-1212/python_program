def firstlast(n):
    l=n%10
    while n>0:
        r=n%10
        n//=10
        f=r
    return f+l
num=int(input("Enter a number: "))
sum=firstlast(num)
print("Sum of first and last digit is:",sum)
