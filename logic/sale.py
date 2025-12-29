from time import strftime

class Sale():
    def __init__(self,chinamo_id, items):
        self.chinamo_id = chinamo_id
        self.items = items
        self.total = self.calculate_total()
        self.timestamp = strftime("%a, %d %b %Y %H:%M:%S")

    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item['qty'] * item['unit_price']
        return total

    def to_dict(self):
        return {
            'chinamo_id': self.chinamo_id,
            'items': self.items,
            'total': self.total,
            'timestamp': self.timestamp
        }


#pruebas
items = [
    {"name": "Empanada", "qty": 3, "unit_price": 500},
    {"name": "Refresco", "qty": 1, "unit_price": 800}
]

sale = Sale("ATB1", items)

sale_dict = sale.to_dict()

