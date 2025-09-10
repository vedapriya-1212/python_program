#print lowest frequency in given string
def lowfreq(str):
    d={}
    for i in str:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    min=str.__len__()
    for i in d:
        if d[i]<min:
            min=d[i]
            c=i
    return c,min
str=input("Enter any string:")
ch,f=lowfreq(str)
print(f"lowest frequency character is '{ch}' with frequency {f}")