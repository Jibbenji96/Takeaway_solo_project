from lib.takeaway import TakeAway
from unittest.mock import Mock
from dotenv import load_dotenv
from twilio.base.exceptions import TwilioRestException
import pytest
import os

load_dotenv()

TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")


def test_takeaway_instantiates_empty_dictionary():
    takeaway = TakeAway("takeaway")
    assert takeaway.dishes == {}

def test_takeaway_show_menu_empty_list_after_instantiation():
    takeaway = TakeAway("takeaway")
    assert list(takeaway.show_menu()) == []

def test_takeaway_add_dish_show_menu_returns_formatted_dish_list():
    chow_mein = Mock()
    chow_mein.name = "Chow Mein"
    chow_mein.price = 1.50  
    chow_mein.number_available = 2

    salt_pepper_chips = Mock()
    salt_pepper_chips.name = "Salt Pepper Chips"
    salt_pepper_chips.price = 0.75
    salt_pepper_chips.number_available = 1

    takeaway = TakeAway("takeaway")
    takeaway.add_dish(chow_mein)
    takeaway.add_dish(salt_pepper_chips)
    assert takeaway.show_menu() == ["Chow Mein: £1.50", "Salt Pepper Chips: £0.75"]


def test_takeaway_receives_order():
    chow_mein = Mock()
    chow_mein.name = "Chow Mein"
    chow_mein.price = 1.50  
    chow_mein.number_available = 2

    salt_pepper_chips = Mock()
    salt_pepper_chips.name = "Salt Pepper Chips"
    salt_pepper_chips.price = 0.75
    salt_pepper_chips.number_available = 1

    takeaway = TakeAway("takeaway")
    takeaway.add_dish(chow_mein)
    takeaway.add_dish(salt_pepper_chips)

    my_order = Mock(takeaway)

    with pytest.raises(TwilioRestException) as e:
        takeaway.receive_order(my_order, +15005550003)
    assert "Unable to create record" in str(e.value)
