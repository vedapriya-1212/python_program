#with args no return
'''
def add(x,y):
    c=a+b
    print(c)
a=10
b=20
add(a,b)
'''
#convert days to years and months
def days(d):
    mon=(1/30)*d
    year=(1/365)*d
    print("no.of months=",round(mon,2))
    print("no.of years=",round(year,2))
day=int(input("enter no.of days:"))
days(day)