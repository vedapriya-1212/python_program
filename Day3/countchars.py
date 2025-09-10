#count no.of alphabet characters,digits and special characters in a string
def count(str):
    ac=0
    dc=0
    sc=0
    for i in str:
        if (i>='a' and i<='z') or (i>='A' and i<='Z'):
            ac+=1
        elif i>='0' and i<='9':
            dc+=1
        else:
            sc+=1
    return ac,dc,sc
str=input("Enter any string:")
a,d,s=count(str)
print(f"count of:\nalphabets={a}\ndigits={d}\nspecial characters={s}")