class Restaurant():
    """A container for making restraunts"""
    
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type
        
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
        self.name.title() + " is a restraunt serving "
        + self.cuisine_type.title() + " cuisine.\nIt features "
        + flavor_profile + " flavors and an atmosphere best enjoyed attired in "
        + attire +  "."
        )
    def restraunt_open(self):
        """Simulate restraunt opening."""
        print(self.name.title() +  " is now open!")
        

your_favorite = Restaurant("el matador", "spanish")
my_favorite = Restaurant("gorgio's", "italian")
moms_favorite = Restaurant("Bob's Burgers", "American hamburger")

your_favorite.restraunt_open()
your_favorite.summary()

my_favorite.restraunt_open()
my_favorite.summary()

moms_favorite.restraunt_open()
moms_favorite.summary()
