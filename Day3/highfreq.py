#print highest frequency in a string
def highfreq(str):
    d={}
    for i in str:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    max=0
    for i in d:
        if d[i]>max:
            max=d[i]
            c=i
    return c,max
str=input("Enter any string:")
ch,f=highfreq(str)
print(f"highest frequency character is '{ch}' with frequency {f}")