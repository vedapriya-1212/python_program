#count occurence of a character in given string
def count(str,ch):
    c=0
    for i in str:
        if i==ch:
            c+=1
    return c
str=input("Enter any string:")
ch=input("Enter any character to find its occurence:")
print(f"'{ch}' occured {count(str,ch)} times in the given string")