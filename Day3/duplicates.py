#count no.of duplicates in the list 
def dupli(l):
    d=[]
    c=0
    for i in l:
        if i in d:
            c+=1
        else:
            d.append(i)
    return c
list=[1,6,2,1,3,4,2,6,3,4,5]
print("No.of duplicates=",dupli(list))
