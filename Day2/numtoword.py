def num_word(n):
    d={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
    s=""
    while n>0:
        r=n%10
        s=d[r]+" "+s
        n//=10
    return s
num=int(input("Enter a number: "))
print("Number in words:",num_word(num))