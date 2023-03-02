import json

# get and load username, if absent, create new username

greet = input("Enter your username to continue.\n>")
filename = greet +'.json'
print(filename)
try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    username = input("I could not find your username.\n" +
        "Please enter your username again to create new user.\n>")
    with open(filename, 'w') as f_obj:
        username = json.dump(username, f_obj)
        print("We'll remember you when you come back, " + username + "!")
        
else:
    print("Welcome back, " + username + "!")
