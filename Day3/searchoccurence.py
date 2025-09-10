#search all occurences of a character in given string
def search(str,ch):
    l=[]
    for i in range(len(str)):
        if str[i]==ch:
            l.append(i)
    return l
str=input("Enter any string:")
ch=input("Enter any character to find its occurence:")
print(f"'{ch}' found at positions {search(str,ch)} in given string")