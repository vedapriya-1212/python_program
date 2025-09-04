def palin(n):
    temp=n
    rev=0
    while n>0:
        r=n%10
        rev=(rev*10)+r
        n//=10
    if temp==rev:
        return True
    return False
num=int(input("Enter a number: "))
if palin(num):
    print(num,"is a palindrome")
else:
    print(num,"is not a palindrome")
