def primefactor(n):
    for i in range(1,n):
        if n%i==0:
            if i>1:
                c=0
                for j in range(2,i):
                    if i%j==0:
                        c+=1
                if c==0:
                    print(i,end=" ")
num=int(input("Enter a number: "))
primefactor(num)