class Car:
    """Simple try to model a car"""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name

class Battery:
    """Describe a battery of an electric car"""

    def __init__(self, battery_size = 75):
        self.battery_size = battery_size

    def get_range(self):
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge")
    
    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100

class ElectricCar(Car):
    """Describe an electric car"""

    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = Battery()

my_tesla = ElectricCar('tesla', 'model S', 2021)

my_tesla.battery_size.get_range()
my_tesla.battery_size.upgrade_battery()
my_tesla.battery_size.get_range()