from User import User
from Suppliers import Suppliers

class Manager(User):
    def __init__(self, first_name, last_name, username, password, suppliers):
        super().__init__(first_name, last_name, username, password)
        
        self.suppliers = suppliers

    
    def use(self, org):
        org.manager_menu(self)
    
    def __str__(self):
        pass

    def manager_menu(self, user):
        while(True):
            print("Welcome to the manager menu {}.".format(self.get_first_name()))
            print('''1. View my details
2. List all your suppliers
3. Manage a particular supplier
4. Logout''')
            y = input("Please enter a choice: ")
            match y:
                case '1':
                    print("{} {}, manager for: ".format(self.get_first_name(), self.get_last_name()))
                    for supplier in self.suppliers:
                        print(supplier.region)
                case '2':
                    print("All suppliers:")
                    for s in self.suppliers:
                        s.supplier_list()
                             
                case '3':
                    while(True):
                        print("Which supplier would you like to manage?")
                        i = 1;
                        for supplier in self.suppliers:
                            print("{}. {}".format(i, supplier.region))
                            i += 1
                        z = input("Supplier: ")
                        try:
                            z = int(z)
                            if 1 <= int(z) <= (i-1):
                                sup1 = self.suppliers[z-1]
                                sup1.manage_supplier(sup1, self)
                                break
                            else:
                                print("No such supplier!")
                        except ValueError:
                            print("Enter a valid number")
                        
                case '4':
                    print("Thanks for using the Prog2 Warehouse Manager. Come again soon!")
                    return
                case default:
                    print("Please enter a valid number, press 4 to logout.")
                    

