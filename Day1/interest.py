p=int(input("Enter principal amount: "))
t=int(input("Enter total no.of months: "))
r=int(input("enter rate of interest: "))
t=t/12
si=(p*t*r)/100
print("Simple interest is: ",si)
a=p+si
print("total amount is: ",a)