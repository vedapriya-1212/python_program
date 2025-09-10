def count(l):
    ec=0
    oc=0
    for i in l:
        if i%2==0:
            ec+=1
        else:
            oc+=1
    return ec,oc
list=[1,2,3,4,5,6,7,8,9]
even,odd=count(list)
print("Even Count=",even)
print("Odd Count=",odd)
    