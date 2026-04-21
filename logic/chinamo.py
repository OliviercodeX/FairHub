class Chinamo:
    products = {}

    def __init__(self, seller_name, chinamo_id=None):
        self.seller_name = seller_name
        self.id = chinamo_id
        if self.id and self.id not in self.products:
            self.products[self.id] = {
                'seller': self.seller_name,
                'products': []
            }

    def add_product(self, product, price):
        if self.id is None:
            return False
        if self.id not in self.products:
            self.products[self.id] = {
                'seller': self.seller_name,
                'products': []
            }
        self.products[self.id]['products'].append({
            'name': product,
            'price_product': price
        })
        return True


    def remove_product(self, product):
        if self.id is None or self.id not in self.products:
            return False
        data_products = self.products[self.id]['products']
        for element in data_products:
            if element['name'].lower() == product.lower():
                data_products.remove(element)
                return True
        return False

    def update_seller_name(self, new_name):
        if self.id is None or self.id not in self.products:
            return False
        self.seller_name = new_name
        self.products[self.id]['seller'] = new_name
        return True

# test1 = Chinamo('Marcos') Esto es código de prueba entonces si lo llego a usar despues
# test1.add_product('Arroz con leche', 500)
# test1.add_product('arroz con pollo', 1500)
# test1.remove_product('arroz con pollo')
# test1.remove_product('arroz con pollo')


# productos = Chinamo.products
# for code, product in productos.items():
#     print(f'{product}\n')