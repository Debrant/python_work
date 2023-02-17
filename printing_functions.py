import time

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design into completed models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
    
        # Simulate 3D printing
        
        print("Printing model: " + current_design)
        time.sleep(0.5)
        print("Printing model: " + current_design)
        time.sleep(0.5)
        print("Printing model: " + current_design) 
        completed_models.append(current_design)
        
    
def show_completed_models(completed_models):
    """ Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
            
