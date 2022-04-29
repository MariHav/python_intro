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