code = 1

class Chinamo:
    
    def __init__(self,seller_name):
        self.seller_name = seller_name
        self.products = {}

    
    def add_product(self,producto, price):
        global code #TODO To fix this method
        self.products[f'ATB{code}'] = {
            'seller' : self.seller_name,
            'nombre' : [producto],
            'precio' : price
        }
        code += 1
        
        print(self.products)

    def remove_product(self):
        global code  #TODO To finish this method
        for key, value in self.products(self.products.keys()):
            pass


    def get_total_stock(self):
        pass

test1 = Chinamo('Marcos')
test1.add_product('Arroz con leche', 500)
test2 = Chinamo('Marcos')
test2.add_product('Arroz con leche', 500)