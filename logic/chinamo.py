
code_list = []
class Chinamo:
    # Variable de CLASE - compartida entre todas las instancias
    products = {}
    
    def __init__(self,seller_name):
        self.seller_name = seller_name
        

    
    def add_product(self,product, price):
        
        seller_code = None
        for code_key, seller_data in self.products.items():
            print(seller_data['seller'])
            if seller_data['seller'] == self.seller_name:
                seller_code = code_key
        
        if seller_code:
            
            self.products[seller_code]['products'].append({
                'name': product,
                'price_product': price
            })
        
        


        else:
            code = f'ATB{len(code_list)+1}'
            self.products[code] = {
                    'seller' : self.seller_name,
                    'products': [{
                        'name': product,
                        'price_product': price
                    }]
                }
            code_list.append('code')

        
        
        
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