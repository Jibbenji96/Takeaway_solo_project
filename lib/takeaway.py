from dotenv import load_dotenv
from datetime import datetime, timedelta
from twilio.rest import Client
import os

class TakeAway:
    def __init__(self, takeaway_name):
        load_dotenv()
        self.dishes = {}
        self.takeaway_name = takeaway_name
        self.account_sid = os.getenv("TWILIO_ACCOUNT_SID")
        self.auth_token = os.getenv("TWILIO_AUTH_TOKEN")
        self.from_number = os.getenv("TWILIO_PHONE_NUMBER")
        self.client = Client(self.account_sid, self.auth_token)


    def add_dish(self, dish):
            if dish.number_available > 0:
                self.dishes[dish.name] = dish.price
                

    def show_menu(self):
        return [f"{item}: £{self.dishes[item]:.2f}" for item in self.dishes]
        
    
    def receive_order(self, myorder, phone_number):
        delivery_time = (datetime.now() + timedelta(minutes=30)).strftime("%H:%M")

        message = self.client.messages.create(
                    body = f"Thank you! Your order was placed and will be delivered before {delivery_time}.",
                    from_ = self.from_number,
                    to = phone_number  
                )
        myorder._clear_order()

        return message.sid
        