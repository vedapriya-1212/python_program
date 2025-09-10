def neg(list):
    nl=[]
    for i in list:
        if i<0:
            nl.append(i)
    return nl    
list1=[1,2,-4,2,-8,-5,3,-1]
print(neg(list1))