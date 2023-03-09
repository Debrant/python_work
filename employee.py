class Employee():
    """A class to track employee wages by name."""
    def __init__(self, full_name='first last', salary=40000):
        self.full_name = full_name.title()
        self.salary = salary
        
        
    
    def update_salary(self):
        """ Allow the base salary to be changed."""
        while True:
            print(self.full_name +"'s base salary is currently: $" + 
                str(self.salary) + ". \nIs this correct?")
            answer = input("\n Type y/n to continue.")
            if answer == 'n':
                self.salary = int(
                    input("Please enter the correct annual salary: $")
                    )
            else:
                print("Salary confirmed, thank you.")
                break
                
    def give_raise(self, annual_raise=5000):
        """ Apply an increase to the annual salary."""
        print(
            "Adding $" + str(annual_raise) + " to " 
            + self.full_name + "'s annual salary."
            )
        self.salary += annual_raise
        print(
            self.full_name +"'s base salary is now: $" + 
             str(self.salary) + "."
             )
        


        
        
        
    
