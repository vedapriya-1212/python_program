def strong(n):
    for i in range(n+1):
        s=0
        temp=i
        for j in range(len(str(i))):
            r=i%10
            f=1
            k=1
            while k<=r:
                f*=k
                k+=1
            s+=f
            i//=10
        if s==temp:
            print(temp,end=" ")
num=int(input("Enter a number: "))
strong(num)