def armstrong(n):
    temp=n
    s=0
    while n>0:
        r=n%10
        s+=r**3
        n//=10
    if s==temp:
        return True
    else:
        return False
num=int(input("Enter a number: "))
if armstrong(num):
    print(num,"is an armstrong number")
else:
    print(num,"is not an armstrong number")