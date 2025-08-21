## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._
As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MyOrder:
    def __init__(self):
        # Parameters:
        #   None
        # Side effects:
        #   Sets the order list property of the self dictionary object
        pass # No code here yet
    
    def add_to_order(self, dish, amount):
        # Parameters:
        #   dish: object representing a dish
        #   amount: integere representing number of instances of dish to order
        # Returns:
        #   Nothing if order fits within constraints, otherwise
        #   returns messages indicating dish is not available for X.
        # Side-effects
        #   Saves the dish to the self order list object
        #   Reduces number of dishes available in takeaway object by amount ordered
        pass # No code here yet    

    def see_order(self):
        # Parameters:
        #   None
        # Returns:
        #   An itemised list of the order, and a total price
        # Side-effects
        #   None
        pass # No code here yet    



class TakeAway:
    # User-facing properties:
    #   name: string

    def __init__(self, takeaway_name):
        # Parameters:
        #   takeaway_name: string representing takeaway name
        # Side effects:
        #   Sets the dishes property of the self dictionary object and name
        pass # No code here yet

    def add_dish(self, dish):
        # Parameters:
        #   dish: object representing a dish
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the dish to the self object
        pass # No code here yet
    
    def show_menu(self):
        # Parameters:
        #   None
        # Returns:
        #   A list of all dishes in takeaway and their prices
        # Side-effects
        #   None
        pass # No code here yet
    
    def receive_order(self, myorder):
        # Parameters:
        #   myorder: object representing an order of dishes
        # Returns:
        #   A twilio text confirmation "Thank you! Your order was placed and will be delivered before {current time + 30 minutes}"
        # Side-effects
        #   Clears the myorder object
        pass # No code here yet

    

class Dish:
    def __init__(self, name, price, number_available):
        # parameters: 
        #   name: a string representing the name of the dish
        #   number_available: integer representing number of those dishees available to order
        #   price: string representing the price
        # returns:
        #   Nothing
        # side-effects:
        #   sets the property of self name object 
        pass
    
    def get_dish_name(self):
        # parameters: 
        #   None 
        # returns:
        #   dish name attribute
        # side-effects:
        #   None
        pass
    
    def get_dish_price(self):
        # parameters: 
        #   None 
        # returns:
        #   dish price attribute
        # side-effects:
        #   None
        pass

    def get_dish_number_available(self):
        # parameters: 
        #   None 
        # returns:
        #   dish number available attribute
        # side-effects:
        #   None
        pass
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given a name 
@Dish stores the dish in an object
"""
chow_mein = Dish("Chow mein", 1.50, 3)

chow_mein.get_dish() # => "Chow mein"

"""
Instantiating a take away
#show_menu returns an empty dishes list
"""
take_away = TakeAway()
take_away.show_menu() # #> []

"""
Given a dish 
#show_menu returns the dish and its price 
"""

chow_mein = Dish("Chow mein", 1.50, 3)
take_away = TakeAway()
take_away.add_dish(chow_mein)
take_away.show_menu() # #> ["Chow Mein : "£1.50"]

"""
Given several dishes
One dish is given no availablity
#show_menu returns the dishes and its prices but excludes the unavailable dish 
"""

chow_mein = Dish("Chow mein")
wonton = Dish("Wonton")
take_away = TakeAway()
take_away.add_dish(chow_mein, 1.50, 3)
take_away.add_dish(wonton, 0.50, 0)

take_away.show_menu() # #> ["Chow Mein" : £1.50]

"""
Instantiating a @MyOrder
@show_order returns an empty dishes list
"""
my_order = MyOrder()
my_order.show_order() # #> []

"""
Adding several dishes
#show_order returns the dishes and its total price 
"""

chow_mein = Dish("Chow mein", 1.50, 3)
wonton = Dish("Wonton", 0.50, 0)
salt_pepper_chips = Dish("Salt PepperChips", 0.75, 2)
take_away = TakeAway()
take_away.add_dish(chow_mein)
take_away.add_dish(wonton)
take_away.add_dish(salt_pepper_chips)

my_order = MyOrder()
my_order.add_to_order(chow_mein, 1)
my_order.add_to_order(salt_pepper_chips, 1)  
my_order.show_order() # #> "There are 2 items in your order: chow mein and salt pepper chips. The total cost is £2.25"


"""
Adding several dishes
#receive_order sends a confirmation text 
"""

chow_mein = Dish("Chow mein", 1.50, 3)
wonton = Dish("Wonton", 0.50, 0)
salt_pepper_chips = Dish("Salt PepperChips", 0.75, 2)
take_away = TakeAway()
take_away.add_dish(chow_mein)
take_away.add_dish(wonton)
take_away.add_dish(salt_pepper_chips)

my_order = MyOrder()
my_order.add_to_order(chow_mein, 1)
my_order.add_to_order(salt_pepper_chips, 1)  
my_order.show_order() # #> "There are 2 items in your order: chow mein and salt pepper chips. The total cost is £2.25"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
