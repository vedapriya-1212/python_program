#input=aaabbca output should be like a4b2c1
def count(str):
    f=[]
    c={}
    for i in str:
        if i not in f:
            f.append(i)
            c[i]=1
        else:
            c[i]+=1
    for i in f:
        print(f"{i}{c[i]}",end="")
str=input("Enter any string:")
d=count(str)