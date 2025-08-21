from lib.my_order import MyOrder
from lib.dish import Dish
from lib.takeaway import TakeAway
from twilio.base.exceptions import TwilioRestException
import pytest

def test_takeaway_integration():
    chow_mein = Dish("Chow mein", 2.50, 3)
    salt_pepper_chips = Dish("Salt Pepper Chips", 1.50, 2)
    wontons = Dish("Wontons", 0.60, 5)

    assert chow_mein.get_dish_name() == "Chow mein"
    assert salt_pepper_chips.get_dish_price() == 1.50
    assert wontons.get_dish_number_available() == 5

    chinese_takeaway = TakeAway("General Tsao")
    chinese_takeaway.add_dish(chow_mein)
    chinese_takeaway.add_dish(salt_pepper_chips)
    chinese_takeaway.add_dish(wontons)

    assert chinese_takeaway.show_menu() == ["Chow mein: £2.50", "Salt Pepper Chips: £1.50", "Wontons: £0.60"]

    my_order = MyOrder(chinese_takeaway)
    my_order.add_to_order(chow_mein, 2)
    my_order.add_to_order(salt_pepper_chips, 1)
    my_order.add_to_order(wontons, 3)

    assert chow_mein.get_dish_number_available() == 1
    assert my_order.see_order() == "Your order from General Tsao is Chow mein: 2, Salt Pepper Chips: 1, Wontons: 3. Total price = £8.30."

    with pytest.raises(TwilioRestException) as e:
        chinese_takeaway.receive_order(my_order, +15005550003)
    assert "Unable to create record" in str(e.value)
    