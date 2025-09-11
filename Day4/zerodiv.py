def div(a,b):
    try:
        print(a/b)
    except ZeroDivisionError:
        print("Error:Zero division error, cannot divide with zero")

a=int(input("Enter any inetger: "))
b=int(input("enter another integer: "))
div(a,b)