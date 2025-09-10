def count(str):
    vc=0
    cc=0
    for i in str:
        if (i=='a'or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vc+=1
        else:
            cc+=1
    return vc,cc
str=input("Enter any string:")
v,c=count(str)
print(f"count of:\nvowels={v}\nconsonants={c}")