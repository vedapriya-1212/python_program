def wordcount(str):
    wc=0
    for i in str:
        if i==" " or i=="\t":
            wc+=1
    return wc+1
str=input("Enter any string:")
print("No.of words in the string is:",wordcount(str))