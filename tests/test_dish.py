from lib.dish import Dish

def test_dish_instantiates():
    dish = Dish("dish", 1.50, 2)
    assert type(dish) == Dish

def test_get_dish_returns_dish_name():
    dish = Dish("dish", 1.50, 2)
    assert dish.get_dish_name() == "dish"

def test_get_dish_returns_dish_price():
    dish = Dish("dish", 1.50, 2)
    assert dish.get_dish_price() == 1.50

def test_get_dish_returns_dish_number_available():
    dish = Dish("dish", 1.50, 2)
    assert dish.get_dish_number_available() == 2

