#display only unique elements from a list
def unique(l):
    unique=[]
    for i in l:
        if i in unique:
            continue
        else:
            unique.append(i)
    print("Unique elements are:",unique)
list=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,1,2,3,1]
unique(list)
