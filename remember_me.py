import json

# get and load username, if absent, create new username

# greet = input("Enter your username to continue.\n>")
# filename = greet +'.json'
# print(filename)
# try:
    # with open(filename) as f_obj:
        # username = json.load(f_obj)
# except FileNotFoundError:
    # username = input("I could not find your username.\n" +
        # "Please enter your username again to create new user.\n>")
    # with open(filename, 'w') as f_obj:
        # username = json.dump(username, f_obj)
        # print("We'll remember you when you come back, " + username + "!")
        
# else:
    # print("Welcome back, " + username + "!")

        
        
def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username
        
    
def get_new_username():
    """Prompt for a new username,"""
    username = input("What is your name?")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        return username
    
        
        
def greet_user():
    """Greet the user by name."""
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you come back, " + username + "!")
        
        
greet_user()
