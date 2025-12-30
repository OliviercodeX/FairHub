from chinamo import *
from sale import *
class Fair_manager():
    def __init__(self):
        self.chinamos = {}
        self.sales = []

    def create_chinamo(self, seller_name):
        get_chinamo = Chinamo(seller_name)

    def add_product_main(self, product, price):
        self.chinamos = Chinamo.add_product(product,price)
        return self.chinamos

    def register_sale(self, chinamo_id, items):

        data_sale = Sale.to_dict(chinamo_id, items)
        

    def get_chinamo_income(self, chinamo_id):
        total_income = 0
        pass

    def save_data():
        pass

    def load_data():
        pass
    
