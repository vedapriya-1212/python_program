def length(str):
    c=0
    for i in str:
        c+=1
    return c
def compare(str1,str2):
    if length(str1)==length(str2):
        print("Both strings are of equal length")
    else:
        print("Strings are of different length")
def concat(str1,str2):
    return str1+str2
str1=input("Enter any string:")
str2=input("Enter another string:")
print("Length of string 1 is:",length(str1))
compare(str1,str2)
print("Concatenated string is:",concat(str1,str2))