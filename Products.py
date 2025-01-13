class Products:
    def __init__(self, products=[]):
        
        if products is None:
            self.products = []
        else:
            self.products = products
