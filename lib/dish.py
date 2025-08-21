class Dish:
    def __init__(self, name, price, number_available):
        self.name = name
        self.price = price
        self.number_available = number_available
    
    def get_dish_name(self):
        return self.name
    
    def get_dish_price(self):
        return self.price

    def get_dish_number_available(self):
        return self.number_available