#program to find first and last digit of a number
def firstlast(n):
    l=n%10
    '''
    while n>0:
        r=n%10
        n//=10
        f=r
    '''
    for i in range(len(str(n))):
        r=n%10
        n//=10
        f=r
    return f,l
num=int(input("Enter a number: "))
first,last=firstlast(num)
print("First digit is:",first)
print("Last digit is:",last)