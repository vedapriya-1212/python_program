def addele(ele):
    if ele not in set1:
        set1.add(ele)
    else:     
        print(f"{ele} already exists in the set")
def show():
    print(set1)
set1=set()
n=int(input("Enter number of elements:"))
for i in range(n):
    ele=int(input(f"Enter element {i+1} to be added:"))
    addele(ele)
show()