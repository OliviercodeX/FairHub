import json
#TODO corregir los metodos ya que no estoy entendiendo el flujo del proyecto
class data_fair_management():
    def __init__(self):
        self.file_path= 'FairHub\data\fair_data.json'

    
    def load_data_files(self):

        with open(self.file_path, 'r') as file:
            json.load(file)

    def save_data_files(self):
        with open(self.file_path, 'w') as file:
            json.dump(file, indent=4)

class data_sales_history():
    def __init__(self):
        self.file_path = 'FairHub\data\sales_history.json'

    def load_data(self):
        with open(self.file_path, 'r') as file:
            json.load(file)

    def save_data(self):
        with open(self.file_path, 'r') as file:
            json.dump(file, indent=4)