class Restaurant:
    """Describe a restaurant"""

    def __init__(self,restaurant_name,cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type

    def describe_restaurant(self):
        print(f"\nMeet our new restaurant '{self.name.title()}' with the best "
        +f"{self.type} cuisine in the city!")

    def open_restaurant(self):
        print(f"\n'{self.name.title()}' is open now.")

oriental_restaurant = Restaurant('Asia','oriental')
italian_restaurant = Restaurant('Rome','italian')
ukrainian_restaurant = Restaurant('Borsch','traditional')

oriental_restaurant.describe_restaurant()
italian_restaurant.describe_restaurant()
ukrainian_restaurant.describe_restaurant()

class IceCreamStand(Restaurant):
    """Describe a specialized restaurant for selling ice cream"""

    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.toppings = ['vanila','chocolate','jam']

    def available_toppings(self):
        print("\nHere is the list of available toppings:")
        for topping in self.toppings:
            print(topping)

new_icecream = IceCreamStand('Lviv','Ice cream')
new_icecream.available_toppings()
    