#library management
def add(bid,title):
    lib[bid]=title
     
def remove(bid):
    del lib[bid]   

def search(bid):
    if bid in lib.keys():
        print(lib[bid])
    else:
        print("None")

def update(bid,title):
    lib[bid]=title

def display():
    print(lib)

def count():
    print(len(lib))

def check(title):
    if title in lib.values():
        print("Available")
    else:
        print("Not available")

lib={}
while True:
    print("1.Add a book")
    print("2.Remove a book using book id")
    print("3.Search a book using id display title")
    print("4.Update title of a book")
    print("5.Display all books in library")
    print("6.count total no.of books")
    print("7.check if book title exists in library")
    print("8.Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        bid=int(input("Enter book id:"))
        title=input("Enter book title:")
        add(bid,title)
    elif choice==2:
        bid=int(input("Enter id to remove:"))
        remove(bid)
    elif choice==3:
        bid=int(input("Enter id to search:"))
        search(bid)
    elif choice==4:
        bid=int(input("Enter id to update:"))
        title=input("Enter new title:")
        update(bid,title)
    elif choice==5:
        display()
    elif choice==6:
        count()
    elif choice==7:
        title=input("Enter title to search")
        check(title)
    elif choice==8:
        break
    else:
        print("Invalid choice try again")


