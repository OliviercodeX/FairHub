from logic.chinamo import Chinamo
from logic.sale import Sale
import json
from pathlib import Path
from time import strftime

DATA_DIR = Path('FairHub/data/storage')
CHINAMOS_FILE = DATA_DIR / 'chinamos.json'
SALES_HISTORY_FILE = DATA_DIR / 'sales_history.json'
FAIR_DATA_FILE = DATA_DIR / 'fair_data.json'

class Fair_manager():
    def __init__(self):
        self.chinamos = {}  # dict con ID como key y objeto Chinamo como value
        self.sales = []  # lista de objetos Sale

    def create_chinamo(self, seller_name):
        chinamo_id = f'ATB{len(self.chinamos) + 1}'
        chinamo = Chinamo(seller_name, chinamo_id)
        self.chinamos[chinamo_id] = chinamo
        return chinamo_id

    def register_sale(self, chinamo_id, items):
        if chinamo_id not in self.chinamos:
            raise ValueError(f"Chinamo {chinamo_id} no existe")
        sale = Sale(chinamo_id, items)
        self.sales.append(sale)
        self.update_fair_data()
        return sale

    def get_chinamo_income(self, chinamo_id):
        total_income = 0
        for sale in self.sales:
            if sale.chinamo_id == chinamo_id:
                total_income += sale.total
        return total_income

    def get_total_sales(self):
        return sum(sale.total for sale in self.sales)

    def get_total_fiados(self):
        return sum(sale.total for sale in self.sales if sale.sale_type == 'fiado')

    def get_total_bought(self):
        return sum(sale.total for sale in self.sales if sale.sale_type == 'bought')

    def get_chinamo_stats(self, chinamo_id):
        total = 0
        fiados = 0
        bought = 0
        for sale in self.sales:
            if sale.chinamo_id == chinamo_id:
                total += sale.total
                if sale.sale_type == 'fiado':
                    fiados += sale.total
                elif sale.sale_type == 'bought':
                    bought += sale.total
        return {'total': total, 'fiados': fiados, 'bought': bought}

    def get_top_chinamos(self):
        chinamo_totals = {}
        for sale in self.sales:
            chinamo_totals[sale.chinamo_id] = chinamo_totals.get(sale.chinamo_id, 0) + sale.total
        return sorted(chinamo_totals, key=chinamo_totals.get, reverse=True)

    def update_fair_data(self):
        fair_data = {
            'total_sales': self.get_total_sales(),
            'total_fiados': self.get_total_fiados(),
            'total_bought': self.get_total_bought(),
            'chinamo_totals': {cid: self.get_chinamo_stats(cid) for cid in self.chinamos},
            'top_chinamos': self.get_top_chinamos(),
            'last_updated': strftime("%a, %d %b %Y %H:%M:%S")
        }
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        with open(FAIR_DATA_FILE, 'w', encoding='utf-8') as f:
            json.dump(fair_data, f, indent=4)

    def add_sale_to_history(self, sale):
        self.sales.append(sale)
        self.update_fair_data()

    def save_data(self):
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        # Guardar chinamos (usando Chinamo.products que es class var)
        chinamos_data = Chinamo.products
        with open(CHINAMOS_FILE, 'w', encoding='utf-8') as f:
            json.dump(chinamos_data, f, indent=4)
        
        # Guardar sales
        sales_data = [sale.to_dict() for sale in self.sales]
        with open(SALES_HISTORY_FILE, 'w', encoding='utf-8') as f:
            json.dump(sales_data, f, indent=4)
        
        # Actualizar estadísticas al guardar
        self.update_fair_data()

    def load_data(self):
        DATA_DIR.mkdir(parents=True, exist_ok=True)
        # Cargar chinamos
        try:
            if CHINAMOS_FILE.exists() and CHINAMOS_FILE.stat().st_size > 0:
                with open(CHINAMOS_FILE, 'r', encoding='utf-8') as f:
                    Chinamo.products = json.load(f)
                for chinamo_id, chinamo_data in Chinamo.products.items():
                    seller_name = chinamo_data.get('seller', '')
                    self.chinamos[chinamo_id] = Chinamo(seller_name, chinamo_id)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        
        # Cargar sales
        try:
            if SALES_HISTORY_FILE.exists() and SALES_HISTORY_FILE.stat().st_size > 0:
                with open(SALES_HISTORY_FILE, 'r', encoding='utf-8') as f:
                    sales_data = json.load(f)
                    for sale_dict in sales_data:
                        sale = Sale(sale_dict['chinamo_id'], sale_dict['items'])
                        sale.sale_type = sale_dict.get('type', 'bought')
                        sale.timestamp = sale_dict.get('timestamp', sale.timestamp)
                        self.sales.append(sale)
        except (FileNotFoundError, json.JSONDecodeError):
            pass
        
        # Actualizar estadísticas después de cargar datos
        self.update_fair_data()
    
