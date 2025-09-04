#sum of factorial of digits is equal to number or not
def strong(n):
    s=0
    temp=n
    while n>0:
        r=n%10
        f=1
        i=1
        while i<=r:
            f*=i
            i+=1
        s+=f
        n//=10
    if s==temp:
        return True
    else:
        return False
num=int(input("Enter a number: "))
if strong(num):
    print(num,"is a strong number")
else:
    print(num,"is not a strong number")