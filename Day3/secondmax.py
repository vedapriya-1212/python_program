'''
def second_max(l):
    max=l[0]
    for i in l:
        if i>max:
            max=i
    l.remove(max)
    secondmax=l[0]
    for i in l:
        if i>secondmax:
            secondmax=i
    return secondmax
list=[1,2,6,1,3,7,8]
print(second_max(list))
'''
def second_max(l):
    l.sort()
    return l[-2]
list=[1,2,6,1,3,7,8]
print(second_max(list))