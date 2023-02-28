#filename = 'programming.txt'

class Memo():
    """A note wrapper."""
    
    def __init__(self):
        self.filename = input("Enter the filename you want save your note as.")
        with open(self.filename, 'w') as file_object:
            file_object.write(input("Enter text to save."))
        
    def add_note(self):
        """append new lines to your note"""
    
        with open(self.filename, 'a') as file_object:
            file_object.write("\n" + input("What do you want to add to your note?"))
        
   
   
        
        
test = Memo()

test.add_note()


