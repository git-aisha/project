from Products import Products
from Product import Product
from Cart import Cart

class Supplier:
    def __init__(self, name, region, address, products):
        self.name = name
        self.region = region
        self.address = address
        self.products = Products(products)
        self.profit = 0
        
    def use(self, user):
        pass
        
    def add_profit(self, amount):
        self.profit += amount

    def disp_profit(self):
        return "Total Profit: {}".format(self.profit)
        
    def manage(self, user):
        pass
        
    def get_region(self):
        return self.region

    def supplier_menu(self,supplier,user):
        cart = Cart(supplier, user)
        while(True):
            print("Welcome to {}".format(supplier.name))
            print('''1. View supplier details
2. View products
3. View profit
4. Order''')
            t = input("Please enter a choice: ")
            match t:
                case '1':
                    print(supplier)
                    self.supplier_menu(supplier, user)
                    return
                case '2':
                    for product in supplier.products.products:
                        print(product)
                case '3':
                    print(supplier.disp_profit())
                case '4':
                    self.order(cart,supplier,user)
                case "X":
                    print("Thanks for shopping at {}".format(supplier.name))
                    user.customer_menu(self)
                    return
                case default:
                    print("Please enter a valid number, or press X to exit.")
                    self.supplier_menu(supplier, user)
                    return

    def supplier_list(self):
        print("{}".format(self))


        
            
            
    def manage_supplier(self,supplier, user):
        cart = Cart(supplier, user)
        while(True):
            print("Welcome to {}".format(supplier.name))
            print('''1. View supplier details
2. View all products
3. View available products
4. Add a product
5. Remove a product
6. Restock a product
7. Delist a product
8. View profit
9. Order''')
            x = input("Please enter a choice: ")
            match x:
                # case '1':
                case '2':
                    for p in supplier.products.products:
                        print(p)
                case '3':
                    for p in supplier.products.products:
                        if p.is_available():
                            print(p)
                case '4':
                    name = input("Name: ")
                    price = input("Price: ")
                    ini = input("Initial stock: ")
                    n = Product(name, price, ini)
                    supplier.products.products.append(n)
                case '5':
                    while(True):
                        name = input("Name: ")
                        temp = None;
                        for p in supplier.products.products:
                            if p.get_name() == name:
                                temp = p
                                break

                        if temp:
                            supplier.products.products.remove(temp)
                            print("{} successfully removed.".format(name))
                            break
                        else:
                            print("No such product. Try again")
                case '6':
                    name = input("Name: ")
                    amt = int(input("Amount: "))
                    for p in supplier.products.products:
                            if p.get_name() == name:
                                p.restock(amt)
                                print("{} successfully updated.".format(name))
                                break
                case '7':
                    name = input("Name: ")
                    for p in supplier.products.products:
                        if p.get_name() == name:
                            p.prune()
                            print("{} successfully delisted.".format(name))
                            break
                case '8':
                    print("Total Profit: 0.00")
                case '9':
                    self.order(cart,supplier,user)
                case 'X':
                    break
                case default:
                    print("Please enter a valid number, or press X to exit.")
                    

    def order(self,cart,supplier,user):
        while(True):
            print("Welcome to the cart menu {}".format(user.get_first_name()))
            print('''1. Add a product to your cart
2. Remove a product from your cart
3. View your order
4. Cancel your order
5. Checkout''')
            j = input("Please enter a choice: ")
            match j:
                case '1':
                    print("Please select a product from the catalogue:")
                    i = 1
                    for p in supplier.products.products:
                        print("{}: {}".format(i,p))
                        i = i + 1
                    c = int(input("Product: ")) - 1
                    a = int(input("Amount: "))
                    s = supplier.products.products[c]
                    if s.has(a):
                        cart.add_product(s, a)
                        print("Product added to cart.")
                    else:
                        print("Not enough stock available!")
                case '2':
                    print("Which item would you like to remove?")
                    i = 1
                    for (p,q) in cart.items:
                        print("{}: {} ({})".format(i,p.get_name(),q))
                        i = i + 1
                    v = int(input("Item: ")) - 1
                    s = cart.items[v][0].get_name()
                    cart.remove_product(s)
                case '3':
                    cart.view_order()
                case '4':
                    print("Order cancelled!")
                    break
                case '5':
                    cart.checkout()
                    
                    break
                case default:
                    print("Please enter a valid number, press 4 to cancel.")
                    
        
    def __str__(self):
        return f"{self.name} ({self.region}), {self.address}"
