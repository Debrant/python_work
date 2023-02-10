# # Store info on pizza being ordered
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
#     }
     
     
#  # summerize order
# print("You ordered a " + pizza['crust'] + "-crust pizza " +
#     "with the folowing toppings:")
    
# for topping in pizza['toppings']:
#     print("\t" + topping)
  

# Start of function work at pg 151

# def make_pizza(*toppings):
#     """Print the list of toppings that have been requeted."""
#     print(toppings)

# make_pizza('pepperoni')
# make_pizza('green peppers', 'mushrooms', 'onions', 'extra cheese')

# Part two
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make"""
    print("\nMaking a pizza with the following toppings:")

    print("\nMaking a " +str(size) + "-inch pizza with the following toppings:")

    for topping in toppings:
        print("- " + topping)


#make_pizza(16, 'pepperoni')
#make_pizza(20, 'green peppers', 'mushrooms', 'onions', 'extra cheese')