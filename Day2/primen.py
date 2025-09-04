def prime(n):
    print(2,end=" ")
    for i in range(3,n+1):
        c=0
        for j in range(2,i):
            if i%j==0:
                c+=1
                break
        if c==0:
            print(i,end=" ")
num=int(input("Enter a number: "))
prime(num)