from car import *
from battery import *


class ElectricCar(Car):
    """Represtent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()
        
    # def describe_battery(self):
        # """Print a statement describing battery size."""
        # print("This car has a " + str(self.battery_size) + " kWh battery.")
        
my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
