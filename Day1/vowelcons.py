#if it is vowel or consonant
def vc(ch):
    l=['a','e','i','o','u','A','E','I','O','U']
    if ch in l:
        print("is vowel")
    else:
        print("is consonant")
c=(input("enter an alphabet:"))
vc(c)  
        