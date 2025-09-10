#user input for appending items to a list
def add(item):
    list1.append(item)
list1=[]
a=int(input("Enter number of elements: "))
for i in range(a):
    item=(input(f"Enter element {i+1} to be added:"))
    add(item)
print("List is:",list1)