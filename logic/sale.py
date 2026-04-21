from time import strftime

class Sale():
    def __init__(self, chinamo_id, items):
        self.chinamo_id = chinamo_id
        self.items = items
        self.total = self.calculate_total()
        self.timestamp = strftime("%a, %d %b %Y %H:%M:%S")
        self.sale_type = 'bought'
        self.debtor_name = None
        # historial de ventas: lista de diccionarios con keys: chinamo_id, items, total, timestamp, type
        self.data_history = []

    def calculate_total(self): 
        total = 0
        for item in self.items:
            total += item['qty'] * item['unit_price']
        return total

    def categorize_sale(self, sale_type='bought', debtor_name=None):
        """Set the sale type and mark each item with the same type.

        Allowed values are 'bought' for immediate payment and 'fiado' for credit.
        """
        if sale_type not in ('bought', 'fiado'):
            raise ValueError("sale_type must be 'bought' or 'fiado'")

        self.sale_type = sale_type
        self.debtor_name = debtor_name if sale_type == 'fiado' else None
        for item in self.items:
            item['type'] = sale_type
        return self.items

    def to_dict(self):
        data_history = {
            'chinamo_id': self.chinamo_id,
            'items': self.items,
            'total': self.total,
            'timestamp': self.timestamp,
            'type': self.sale_type,
            'debtor_name': self.debtor_name
        }
        return data_history

    def get_income_chinamo(self, chinamo_id):
        total_income = 0

        for sale in self.data_history:
            if sale['chinamo_id'] == chinamo_id:
                total_income += sale['total']
        return f' el total del cliente es de {total_income}'
        

# #pruebas
# items = [p
#     {"name": "Empanada", "qty": 3, "unit_price": 500},
#     {"name": "Refresco", "qty": 3, "unit_price": 800}
# ]

# if __name__ == '__main__': tests files
#     sale = Sale("ATB1", items)
#     sala2 = Sale("ATB2", items)
#     sale.data_history = [sale.to_dict(), sala2.to_dict()]
#     print(sale.get_income_chinamo('ATB2'))

#     sale_dict = sale.to_dict()
 
