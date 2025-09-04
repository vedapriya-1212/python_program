def palin(n):
    for i in range(11,n+1):
        temp=i
        rev=0
        for j in range(len(str(i))):
            r=i%10
            rev=(rev*10)+r
            i//=10
        if temp==rev:
            print(temp,end=" ")
        
palin(150)