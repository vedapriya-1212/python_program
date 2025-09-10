#count frequency of each element in a list
def frequency(l):
    freq={}
    for i in l:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
    return freq
list=[1,2,3,4,5,6,7,8,9,1,2,3,4,5,1,2,3,1]
print(frequency(list))