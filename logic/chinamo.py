
code_list = []
class Chinamo:
    # Variable de CLASE - compartida entre todas las instancias
    products = {}
  #TODO Eliminar prints  
    def __init__(self,seller_name):
        self.seller_name = seller_name
        
    def add_product(self,product, price):
        
        seller_code = None
        for code_key, seller_data in self.products.items():

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


    def remove_product(self,product): 

         for code_key, seller_data in self.products.items(): #iterate over the dict self.products

             if seller_data['seller'] == self.seller_name: #if we find the name seller we put a key to access after
                 seller_code = code_key

        
         data_products = self.products[seller_code]['products'] #get the list products with the prices
         finded = False #the flag for validate if we delete the product or doesn't exist
         for elemt in data_products:
            if elemt['name'] == product:
                 finded = True
                 data_products.remove(elemt) #remove the element
                 print('Eliminación correcta')
                 return finded
         if not finded:
             return finded
         

# test1 = Chinamo('Marcos') Esto es código de prueba entonces si lo llego a usar despues
# test1.add_product('Arroz con leche', 500)
# test1.add_product('arroz con pollo', 1500)
# test1.remove_product('arroz con pollo')
# test1.remove_product('arroz con pollo')


# productos = Chinamo.products
# for code, product in productos.items():
#     print(f'{product}\n')