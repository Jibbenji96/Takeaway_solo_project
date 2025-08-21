from lib.my_order import MyOrder
from unittest.mock import Mock
import pytest

def test_myorder_instantiates_empty_list():
    takeaway = Mock()
    my_order = MyOrder(takeaway)
    assert my_order.order_dict == {}


def test_myorder_adds_dish_object_to_order_list():
    
    chow_mein = Mock()
    chow_mein.name = "Chow mein"
    chow_mein.price = 1.50
    chow_mein.number_available = 2

    takeaway = Mock()
    takeaway.takeaway_name = "takeaway"
    takeaway.dishes = {chow_mein.name: chow_mein.price}

    my_order = MyOrder(takeaway)
    my_order.add_to_order(chow_mein, 2)

    assert chow_mein.number_available == 0  
    assert my_order.order_dict == {chow_mein: 2}


def test_myorder_takes_multiple_dish_additions():
    
    chow_mein = Mock()
    chow_mein.name = "Chow mein"
    chow_mein.price = 1.50
    chow_mein.number_available = 2

    salt_pepper_chips = Mock()
    salt_pepper_chips.name = "Salt Pepper Chips"
    salt_pepper_chips.price = 0.50
    salt_pepper_chips.number_available = 1

    takeaway = Mock()
    takeaway.takeaway_name = "takeaway"
    takeaway.dishes = {chow_mein.name: chow_mein.price, salt_pepper_chips.name: salt_pepper_chips.price}

    my_order = MyOrder(takeaway)

    my_order.add_to_order(chow_mein, 1)
    my_order.add_to_order(salt_pepper_chips, 1)
    
    assert chow_mein.number_available == 1
    assert salt_pepper_chips.number_available == 0
    assert my_order.order_dict == {chow_mein : 1, salt_pepper_chips: 1}


def test_myorder_see_order_returns_formatted_string():
    
    chow_mein = Mock()
    chow_mein.name = "Chow mein"
    chow_mein.price = 1.50
    chow_mein.number_available = 2

    salt_pepper_chips = Mock()
    
    salt_pepper_chips.name = "Salt Pepper Chips"
    salt_pepper_chips.price = 0.50
    salt_pepper_chips.number_available = 1

    takeaway = Mock()
    takeaway.takeaway_name = "takeaway"
    takeaway.dishes = {chow_mein.name: chow_mein.price, salt_pepper_chips.name: salt_pepper_chips.price}

    my_order = MyOrder(takeaway)

    my_order.add_to_order(chow_mein, 1)
    my_order.add_to_order(salt_pepper_chips, 1)
    
    assert my_order.see_order() == "Your order from takeaway is Chow mein: 1, Salt Pepper Chips: 1. Total price = £2.00."


def test_myorder_returns_exception_to_incorrect_dish_amount():
    chow_mein = Mock()
    chow_mein.name = "Chow mein"
    chow_mein.price = 1.50
    chow_mein.number_available = 1

    takeaway = Mock()
    takeaway.takeaway_name = "takeaway"
    takeaway.dishes = {chow_mein.name: chow_mein.price}

    my_order = MyOrder(takeaway)
    with pytest.raises(Exception) as e:
        my_order.add_to_order(chow_mein, 2)
    assert str(e.value) == "Only 1 of Chow mein available."


def test_myorder_returns_exception_to_noexistent_dish():
    chow_mein = Mock()
    chow_mein.name = "Chow mein"
    
    salt_pepper_chips = Mock()
    salt_pepper_chips.name = "Salt Pepper Chips"
    salt_pepper_chips.price = 0.50
    salt_pepper_chips.number_available = 1

    takeaway = Mock()
    takeaway.takeaway_name = "takeaway"
    takeaway.dishes = {salt_pepper_chips.name: salt_pepper_chips.price}

    my_order = MyOrder(takeaway)
    with pytest.raises(Exception) as e:
        my_order.add_to_order(chow_mein, 2)
    assert str(e.value) == "Chow mein not available at takeaway."

