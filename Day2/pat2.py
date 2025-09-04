#pattern to print diagonal dollars with remaining stars
def pattern(n):
    for i in range(n):
        for j in range(n):
            if i==j:
                print("$",end=" ")
            else:
                print("*",end=" ")
        print()
num=int(input("Enter number of rows: "))
pattern(num)