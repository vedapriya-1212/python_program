#check whether the given character is alphabet or digit or special character
'''
def checkchar(ch):
    if (ch>='a' and ch<='z') or (ch>='A' and ch<='Z'):
        return "Alphabet"
    elif ch>='0' and ch<='9':
        return "Digit"
    else:
        return "Special Character"
print(checkchar('a')) 
print(checkchar('G'))  
print(checkchar('5'))  
print(checkchar('@'))  
print(checkchar(' ')) 
'''
def checkchar(ch):
    if ch.isalpha():
        return "Alphabet"
    elif ch.isdigit():
        return "Digit"
    else:
        return "Special Character"
print(checkchar('a'))
print(checkchar('5'))
print(checkchar('@'))