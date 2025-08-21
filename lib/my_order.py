class MyOrder:
    def __init__(self, takeaway):
        self.order_dict = {}
        self.takeaway = takeaway

    def add_to_order(self, dish, amount):
        if dish.name not in self.takeaway.dishes:
                raise Exception(f"{dish.name} not available at {self.takeaway.takeaway_name}.")
        
        if amount > dish.number_available:
            raise Exception(f"Only {dish.number_available} of {dish.name} available.")
        
        self.order_dict[dish] = amount
        dish.number_available -= amount
        
    def see_order(self):
        total_price = sum(dish.price * self.order_dict[dish] for dish in self.order_dict)
        order_summary = [f"{dish.name}: {self.order_dict[dish]}" for dish in self.order_dict]

        return f"Your order from {self.takeaway.takeaway_name} is {', '.join(order_summary)}. Total price = £{total_price:.2f}."
    
    def _clear_order(self):
        self.order_dict.clear()