'''
def pattern(n):
    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print()
num=int(input("Enter number of rows: "))
pattern(num)
'''
def pattern(n):
    for i in range(n):
        for j in range(n):
            if i==0 or i==n-1:
                print("*",end=" ")
            elif j==0 or j==n-1:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
num=int(input("Enter number of rows: "))
pattern(num)