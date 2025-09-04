def digits(n):
    s=0
    '''
    while n>0:
        r=n%10
        s+=r
        n//=10
    '''
    for i in range(len(str(n))):
        r=n%10
        s+=r
        n//=10
    return s
num=int(input("Enter a number: "))
print("Sum of digits of",num,"is:",digits(num))