def dupli(l):
    d=[]
    for i in l:
        if i in d:
            continue
        else:
            d.append(i)
    return d
list=[1,6,2,1,3,4,2,6,3,4,5]
print("after removing deplicates:",dupli(list))