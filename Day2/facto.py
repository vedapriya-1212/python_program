def factorial(n):
    f=1
    i=1
    while i<=n:
        f*=i
        i+=1
    return f
num=int(input("Enter a number: ")) 
print("Factorial of",num,"is:",factorial(num))