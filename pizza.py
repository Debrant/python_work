# Store info on pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
     
     
 # summerize order
print("You ordered a " + pizza['crust'] + "-crust pizza " +
    "with the folowing toppings:")
    
for topping in pizza['toppings']:
    print("\t" + topping)
