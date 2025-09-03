# which is greater in 3 numbers
def greater(a,b,c):
    if a>b:
        if a>c:
            print(a,"is big")
        else:
            print(c,"is big")
    else:
        if b>c:
            print(b,"is big")
        else:
            print(c,"is big")
greater(2,3,4)
greater(4,7,3)
greater(8,4,1)