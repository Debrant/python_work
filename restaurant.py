class Restaurant():
    """A container for making restaurant"""
    
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def summary(self):
        """Make a brief summary line for review site entry."""
        flavor_provile = "-"
        attire = ""
        if self.cuisine_type == 'italian':
            flavor_profile = "robust"
            attire = "collared shirts or better"
        elif self.cuisine_type == 'spanish':
            flavor_profile = "pepper forward"
            attire = "professional or formal dress only"
        else:
            flavor_profile = "mild"
            attire = "casual wear"
        
        print(
        self.name.title() + " is a restaurant serving "
        + self.cuisine_type.title() + " cuisine.\nIt features "
        + flavor_profile + " flavors and an atmosphere best enjoyed attired in "
        + attire +  "."
        )
    def restraunt_open(self):
        """Simulate restaurant opening."""
        print(self.name.title() +  " is now open!")
        
    
    def print_number_served(self):
        """Print the number of customers served this shift."""
        print(str(self.number_served) + " customers have eaten here tonight.")
        
        
    def set_number_served(self, customers):
        """
        Set the number of customers served.
        Reject change if it isn't positive.
        """
        if customers >= self.number_served:
            self.number_served = customers
        else:
            print("You can't count backward!")
    
    
    def increment_number_served(self, diners):
        """Add the given milage to the odometer reading."""
        self.number_served += diners
   
        

# your_favorite = Restaurant("el matador", "spanish")
# my_favorite = Restaurant("gorgio's", "italian")
# moms_favorite = Restaurant("Bob's Burgers", "American hamburger")

# your_favorite.restraunt_open()
# your_favorite.summary()

# my_favorite.restraunt_open()
# my_favorite.summary()

# moms_favorite.restraunt_open()
# moms_favorite.summary()

# moms_favorite.set_number_served(27)
# moms_favorite.print_number_served()
# moms_favorite.increment_number_served(10)
# moms_favorite.print_number_served()
