from Order import Order
from User import User


class Cart:
    def __init__(self, supplier, user):
        
        self.supplier = supplier
        self.user = user
        self.items = []
    
    def use(self):
        pass

    def add_product(self,product,amount):
        self.items.append((product,amount))

    def view_order(self):
        t = 0
        print("Order from {}: ".format(self.supplier.region))
        for p,q in self.items:
            print("{} ({})".format(p.get_name(),q))
            t += p.get_price()*q
        from Manager import Manager
        if isinstance(self.user, Manager):
            print("Total Cost: 0.00")
        else:
            self.supplier.add_profit(t)
            print("Total Cost: {:.2f}".format(t))

    def remove_product(self,product):
        for i,(p,q) in enumerate(self.items):
            if p.get_name() == product:
                self.items.pop(i)
                return

    def checkout(self):
        cost = sum(p.get_price()*q for p,q in self.items)
        self.user.add_purchase(self)
        for(p,q) in self.items:
            p.sell(q)
        
        
        return cost
    
    def __str__(self):
        pass
