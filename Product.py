class Product:
    def __init__(self, name, price, initialStock):
        
        self.name = name
        self.price = float(price)
        self.stock = int(initialStock)
        self.delist = False
    
    def get_name(self):
        return self.name
    
    def get_price(self):
        return self.price
    
    def is_available(self):
        return self.stock > 0 and not self.delist
    
    def has(self, stock):
        return self.stock > stock
    
    def sell(self, amount):
        self.stock -= amount
        return self.stock * amount
    
    def restock(self, amount):
        self.stock += amount
    
    def prune(self):
        self.delist = True

    def delist(self):
        pass
    
    def __str__(self):
        return f"{self.name} at ${self.price:.2f} ({self.stock})"
