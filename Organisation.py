from Suppliers import Suppliers
from Users import Users
from InvalidUserError import InvalidUserError
from Manager import Manager
from Product import Product
from Cart import Cart

class Organisation:
    def __init__(self, suppliers, users):
        self.suppliers = suppliers
        self.users = users
    
    def use(self):
        print("Welcome to the Prog2 Warehouse Manager")
        print("Please login below:")
        while(True):
            username = input("Username: ")
            password = input("Password: ")
            try:
                user = self.users.validate_user(username,password)
                if isinstance(user, Manager):
                    user.manager_menu(self)
                else:
                    user.customer_menu(self)
                break
            except InvalidUserError:
                a = input("No user found! Try again? (y/n): ")
                if(a == "y"):
                    print("Please login below:")
                    continue
                elif(a == "n"):
                    print("Thanks for using the Prog2 Warehouse Manager. Come again soon!")
                    return

    

    
    def shop_menu(self,user):
        print("Where would you like to shop?")
        i = 1
        while(i < 19):
            for supplier in (self.suppliers.suppliers):
                print("{}: {}".format(i, supplier.region))
                i += 1

        shop = int(input("Enter a choice: "))
        if 1 <= shop <= 18:
            sup = self.suppliers.suppliers[shop - 1]
            sup.supplier_menu(sup, user)
        else:
            print("Invalid option entered!")
            self.shop_menu(user)

    

    

    
        

if __name__ == "__main__":
    seeded_suppliers = Suppliers().seed_data()
    seeded_users = Users().seed_data(seeded_suppliers)
    Organisation(seeded_suppliers, seeded_users).use()



