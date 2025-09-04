def armstrong(n):
    for i in range(1,n+1):
        temp=i
        s=0
        for j in range(len(str(i))):
            r=i%10
            s+=r**3
            i//=10
        if s==temp:
            print(temp,end=" ")
armstrong(500)