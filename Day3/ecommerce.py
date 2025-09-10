def add(item):
    if item in cart:
        print("Product already in the cart")
    else:
        cart.append(item)
        print(f"{item} added to the cart")
def remove(item):
    if item not in cart:
        print("Product not found in the cart")
    else:
        cart.remove(item)
        print(f"{item} removed from the cart")
def search(item):
    if item in cart:
        print(f"{item} is present in the cart")
    else:
        print(f"{item} is not present in the cart")
def display():
    if not cart:
        print("Cart is empty")
    else:
        print("Products in the cart:", cart)
def total():
    print("Total number of products in the cart:", len(cart))
def sortcart():
    cart.sort()
    print("Products sorted in alphabetical order:", cart)
def clearcart():
    cart.clear()
    print("Cart cleared")
cart=[]
while True:
    print("1.Add product to cart")
    print("2.Remove product from cart")
    print("3.Search for a product in the cart")
    print("4.Display all products in the cart")
    print("5.Show the total number of products in the cart")
    print("6.Sort Products in alphabetical order")
    print("7.Clear the cart")
    print("8.Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        prod=input("Enter product to be added:")
        add(prod)
    elif choice==2:
        prod=input("Enter product to be removed:")
        remove(prod)
    elif choice==3:
        prod=input("Enter product to be searched:")
        search(prod)
    elif choice==4:
        display()
    elif choice==5:
        total()
    elif choice==6:
        sortcart()
    elif choice==7:
        clearcart()
    elif choice==8:
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again")
    print()
    