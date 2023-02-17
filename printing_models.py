from printing_functions import print_models as pm
from printing_functions import show_completed_models as scm
import time


# Set flag to indicate that polling is active
polling_active = True

unprinted_designs = []
completed_models = []

while polling_active:
    # Prompt for the person's name and response
    unprinted_designs.append(input("\nEnter the model you want printed.\n"))
    
    # Find out if anyone else will take the poll
    repeat = input("Would you like to print another model? (yes/ no)")
    if repeat == 'no':
        polling_active = False

print("Models accepted, pleas wait while the printer warms up.")
#print(unprinted_designs)
time.sleep(1)

# Simulate printing the models
pm(unprinted_designs, completed_models)

# Print the completed models
scm(completed_models)



