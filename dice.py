from random import randint
from collections import OrderedDict

class DieSet():
    """Simulate rollable dice determined by number of sides."""
    
    def __init__(self, sides, nd=1):
        """Init each die."""
        self.sides = sides
        self.nd = nd
        self.total = 0
        
        
    def roll_one(self):
        """Roll one die instance."""
        return randint(1, self.sides)
        
        
    
    def dungeon_roll(self, nd):
        """Let the user specify the number of dice to roll."""
        self.nd = nd
        self.total = 0
        for n in range(self.nd):
            self.total = self.total + randint(1, self.sides)
            
        return self.total
        # print("Rolling " + str(self.nd) + "d"+ str(self.sides))
        # print("\nYou rolled " + str(self.total) +"!")
        
        
        
        
        
        
d4 = DieSet(4)        
d6 = DieSet(6)
d8 = DieSet(8)
d10 = DieSet(10)
# d6.roll_one()

# d6.dungeon_roll(3)

def roll_npc(NAME, role):
    """A quick character generator"""
    stats = OrderedDict()
    
    stats['Str'] = d6.dungeon_roll(3) 
    stats['Dex'] = d6.dungeon_roll(3)
    stats['Con'] = d6.dungeon_roll(3)
    stats['Int'] = d6.dungeon_roll(3)
    stats['Wis'] = d6.dungeon_roll(3)
    stats['Cha'] = d6.dungeon_roll(3)
    
    if role.lower() =='fighter':
        stats['HP'] = d10.roll_one()
        
    elif role.lower() == 'ranger':
        stats['HP'] = d8.roll_one()
        
    elif role.lower() == 'mage':
        stats['HP'] = d4.roll_one()
        
    else:
        stats['HP'] = d6.roll_one()
        
    print(NAME.title() + "is a " + role.title() + " with the following stats:")
   
    for name, value in stats.items():
        print(name.upper() + "::  " + str(value))
        
        
        
def roll_champion(NAME, role):
    """A quick character generator"""
    stats = OrderedDict()
    
    stats['Str'] = d6.dungeon_roll(2) + 6
    stats['Dex'] = d6.dungeon_roll(2) + 6 
    stats['Con'] = d6.dungeon_roll(2) + 6
    stats['Int'] = d6.dungeon_roll(2) + 6
    stats['Wis'] = d6.dungeon_roll(2) + 6
    stats['Cha'] = d6.dungeon_roll(2) + 6
    
    if role.lower() =='fighter':
        stats['HP'] = d8.roll_one() + 3
        
    elif role.lower() == 'ranger':
        stats['HP'] = d8.roll_one() + 1
        
    elif role.lower() == 'mage':
        stats['HP'] = d4.roll_one() + 2
        
    else:
        stats['HP'] = d6.roll_one() + 1
        
    print(NAME.title() + "is a " + role.title() + " with the following stats:")
   
    for name, value in stats.items():
        print(name.upper() + "::  " + str(value))
         
        
roll_champion(input("Name your character.\n"), input("What is their class?\n"))
