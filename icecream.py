from restaurant import Restaurant


class IceCreamStand(Restaurant):
    """A specific type of restaurant that serves ice cream."""
    
    def __init__(self, name, cuisine_type='ice_cream'):
        """Initialize parent attributes then add falvors."""
        super().__init__(name, cuisine_type)
        self.flavors =[]
        
        
    def display_flavors(self):
        """Simulate the menue of flavors."""
        print("This month's flavors ...")
        for flavor in self.flavors:
            print("\n... " + flavor.title())
            
            
scoops = IceCreamStand('Scoops of Delight')
scoops.flavors = [
'dark chocolate chunk', 'raw toasted vanilla', 
'caramel butter pecan', 'lavender and malted strawberry swirl '
]


scoops.summary()
scoops.display_flavors()
