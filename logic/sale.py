from time import strftime

class Chinamo():
    def __init__(self,chinamo_id, amount):
        self.chinamo_id = chinamo_id
        self.amount = amount
        self.timestamp = strftime("%a, %d %b %Y %H:%M:%S")

    def to_dict(self):
        pass

