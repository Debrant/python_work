# Set up function
def describe_pet(animal_type, pet_name):
    """Display information about a pet"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
# Set flag to indicate that polling is active
polling_active = True

while polling_active:
    # Prompt for the person's name and response
    name = input("\nWhat is the name of your pet?")
    animal = input("What type of animal is your pet?")
    
    # Store the response in the dictionary
    describe_pet(animal, name)
    
    # Find out if anyone else will take the poll
    repeat = input("Would you like to let another person respond? (yes/ no)")
    if repeat == 'no':
        print("Thank you, have a good day!")
        polling_active = False
    
    
    
