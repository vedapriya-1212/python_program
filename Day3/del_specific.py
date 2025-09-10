def delete(l,index):
    for i in range(len(l)):
        if i==index:
            for j in range(i,len(l)-1):
                l[j]=l[j+1]
            l.pop()     
    return l
list=[1,2,3,4,5,6,7,8,9]
i=int(input("enter position to be deleted:"))
d=delete(list,i)
print(d)