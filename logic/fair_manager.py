from logic.chinamo import Chinamo
from logic.sale import Sale
import json
from pathlib import Path
from time import strftime

DATA_DIR = Path('FairHub/data/storage')
CHINAMOS_FILE = DATA_DIR / 'chinamos.json'
SALES_HISTORY_FILE = DATA_DIR / 'sales_history.json'
FAIR_DATA_FILE = DATA_DIR / 'fair_data.json'
FIADOS_FILE = DATA_DIR / 'fiados.json'

class Fair_manager():
    def __init__(self):
        self.chinamos = {}  # dict con ID como key y objeto Chinamo como value
        self.sales = []  # lista de objetos Sale
        self.fiados = []  # deudas activas

    def create_chinamo(self, seller_name):
        chinamo_id = f'ATB{len(self.chinamos) + 1}'
        chinamo = Chinamo(seller_name, chinamo_id)
        self.chinamos[chinamo_id] = chinamo
        return chinamo_id

    def remove_chinamo(self, chinamo_id):
        if chinamo_id not in self.chinamos:
            return False

        del self.chinamos[chinamo_id]
        Chinamo.products.pop(chinamo_id, None)
        self.sales = [sale for sale in self.sales if sale.chinamo_id != chinamo_id]
        cleaned_fiados = []
        for fiado in self.fiados:
            filtered_items = [
                item for item in fiado.get('items', [])
                if item.get('chinamo_id') != chinamo_id
            ]
            if not filtered_items:
                continue
            fiado['items'] = filtered_items
            fiado['total'] = sum(item.get('total', 0) for item in filtered_items if not item.get('paid'))
            if fiado['total'] > 0:
                cleaned_fiados.append(fiado)
        self.fiados = cleaned_fiados
        return True

    def remove_product_from_chinamo(self, chinamo_id, product_index):
        if chinamo_id not in self.chinamos:
            return False

        chinamo_data = Chinamo.products.get(chinamo_id)
        if not chinamo_data:
            return False

        products = chinamo_data.get('products', [])
        if product_index < 0 or product_index >= len(products):
            return False

        products.pop(product_index)
        return True

    def register_sale(self, chinamo_id, items):
        if chinamo_id not in self.chinamos:
            raise ValueError(f"Chinamo {chinamo_id} no existe")
        sale = Sale(chinamo_id, items)
        self.sales.append(sale)
        self.update_fair_data()
        return sale

    def remove_sale(self, sale_index):
        if sale_index < 0 or sale_index >= len(self.sales):
            return False
        self.sales.pop(sale_index)
        self.update_fair_data()
        return True

    def debtor_name_exists(self, debtor_name):
        debtor_name_norm = debtor_name.strip().lower()
        return any(entry.get('debtor_name', '').strip().lower() == debtor_name_norm for entry in self.fiados)

    def add_fiado(self, debtor_name, items, allow_existing=False):
        debtor_name = debtor_name.strip()
        if not debtor_name:
            raise ValueError('El nombre del fiado es obligatorio')
        existing_entry = next(
            (entry for entry in self.fiados if entry.get('debtor_name', '').strip().lower() == debtor_name.lower()),
            None
        )
        if existing_entry and not allow_existing:
            raise ValueError('Ese nombre de fiado ya existe')

        fiado_items = []
        for item in items:
            total_price = item['qty'] * item['unit_price']
            fiado_items.append({
                'chinamo_id': item['chinamo_id'],
                'name': item['name'],
                'qty': item['qty'],
                'unit_price': item['unit_price'],
                'total': total_price,
                'paid': False
            })

        if existing_entry and allow_existing:
            existing_entry['items'].extend(fiado_items)
            existing_entry['total'] = sum(element['total'] for element in existing_entry['items'] if not element.get('paid'))
            existing_entry['timestamp'] = strftime("%a, %d %b %Y %H:%M:%S")
            return existing_entry

        entry = {
            'id': f"FIADO{len(self.fiados) + 1}",
            'debtor_name': debtor_name,
            'items': fiado_items,
            'total': sum(element['total'] for element in fiado_items),
            'timestamp': strftime("%a, %d %b %Y %H:%M:%S")
        }
        self.fiados.append(entry)
        return entry

    def get_fiados(self):
        return self.fiados

    def mark_fiado_item_paid(self, fiado_id, item_index):
        for entry in self.fiados:
            if entry.get('id') == fiado_id:
                items = entry.get('items', [])
                if item_index < 0 or item_index >= len(items):
                    return False
                items[item_index]['paid'] = True
                entry['total'] = sum(item.get('total', 0) for item in items if not item.get('paid'))
                if all(item.get('paid', False) for item in items):
                    self.fiados = [fiado for fiado in self.fiados if fiado.get('id') != fiado_id]
                return True
        return False

    def get_chinamo_income(self, chinamo_id):
        total_income = 0
        for sale in self.sales:
            if sale.chinamo_id == chinamo_id:
                total_income += sale.total
        return total_income

    def get_total_sales(self):
        return sum(sale.total for sale in self.sales)

    def get_total_fiados(self):
        return sum(entry.get('total', 0) for entry in self.fiados)

    def get_total_bought(self):
        return sum(sale.total for sale in self.sales if sale.sale_type == 'bought')

    def get_total_sinpe(self):
        return sum(
            sale.total for sale in self.sales
            if sale.sale_type == 'bought' and getattr(sale, 'payment_method', 'efectivo') == 'sinpe'
        )

    def get_sales(self, payment_method=None):
        if payment_method is None:
            return self.sales
        return [sale for sale in self.sales if getattr(sale, 'payment_method', 'efectivo') == payment_method]

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
            'total_sinpe': self.get_total_sinpe(),
            'fiados_activos': len(self.fiados),
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

        with open(FIADOS_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.fiados, f, indent=4)
        
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
                        sale.debtor_name = sale_dict.get('debtor_name')
                        sale.payment_method = sale_dict.get('payment_method', 'efectivo')
                        sale.payer_name = sale_dict.get('payer_name')
                        sale.timestamp = sale_dict.get('timestamp', sale.timestamp)
                        self.sales.append(sale)
        except (FileNotFoundError, json.JSONDecodeError):
            pass

        # Cargar fiados activos
        try:
            if FIADOS_FILE.exists() and FIADOS_FILE.stat().st_size > 0:
                with open(FIADOS_FILE, 'r', encoding='utf-8') as f:
                    self.fiados = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.fiados = []
        
        # Actualizar estadísticas después de cargar datos
        self.update_fair_data()
    
