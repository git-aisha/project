from User import User

class Customer(User):
    def __init__(self, first_name, last_name, username, password):
        super().__init__(first_name, last_name, username, password)
    
    def use(self, org):
        self.customer_menu(org)

    def customer_menu(self, org):
        while(True):
            print("Welcome to the customer menu {}.".format(self.get_first_name()))
            print("1. View my details")
            print("2. Shop")
            print("3. View my order history")
            print("4. Logout")
            choice = input("Please enter a choice: ")

            match choice:
                case '1':
                    print("{} {}".format(self.get_first_name(), self.get_last_name()))
                    self.customer_menu(self)
                    return
                case "2":
                    org.shop_menu(self)
                    return
                case "3":
                    if not self.purchases:
                        print("No items purchased")
                    else:
                        for cart in self.purchases:
                            print("Order from {}: ".format(cart.supplier.region))
                            t = 0
                            for p,q in cart.items:
                                print("{} ({})".format(p.get_name(),q))
                                t += p.price*q
                            print("Total Cost: {:.2f}".format(t))
                    
                case "4":
                    print("Thanks for using the Prog2 Warehouse Manager. Come again soon!")
                    return
                case default:
                    print("Please enter a valid number, press 4 to logout.")
                    

    
    def __str__(self):
        pass
