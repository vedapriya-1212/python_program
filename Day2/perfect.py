#check whether sum of divisors of a number is equal to number or not
def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    if s==n:
        print(n,"is a perfect number")
    else:
        print(n,"is not a perfect number")
num=int(input("Enter a number: "))
perfect(num)