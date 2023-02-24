class User():
    """A user container."""
    users =['admin']
    
    def __init__(self):
        """greet user and get user info."""
        self.username = input("""
        Welcome to RobCo usernet! 
        Please enter your username to login.
        """)
        self.last_name = "last"
        self.first_name = "first"
        self.password = "password"
        self.age = 18
        self.role = "employee"
        self.setup_check = False
        self.logged_in = False
        
    def user_login(self, user_name):
        "Let the user login to view their profile."""
        
        if self.setup_check == True:
            count = 0
            temp_pw = input('\nEnter password to log in.\n')
            while count <= 2:
                if temp_pw != self.password:
                    print("""
                    Sorry, your password doesn't match our records.
                    Pleas try agian
                    """)
                    count += 1
                else:
                    ("""        
                    Welcom to RobCo usernet!
                    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                    """)
            self.logged_in = True
            while self.logged_in:
                print("""
                1: See user account summary.
                2:   Change password.
                3:   Edit username.
                4:   Edit age.
                5:   Edit job title.
                6:   Exit usernet.
                """)
                
                next_action = input("Enter selection number to continue.")
                if next_action == '6':
                    self.logged_in = False
                
                elif next_action == '1':
                    print("Name: " + self.first_name.title() + 
                    " " + self.last_name.title())
                    print("\n Username: " + self.username)
                    print( "\nAge: " + str(self.age))
                    print("\nTitle: " + self.role.title())
                    next_action = input("Enter selection number to continue.")
                
                elif next_action == '2':
                    current_pw = input("Enter current password.")
                    while count <= 2:
                        if current_pw == self.password:
                            temp_pw1 = input("Enter new password.")
                            temp_pw2 = input("Confirm new password.")
                            if temp_pw1 == temp_pw2:
                                self.password = temp_password
                            else:
                                print("""
                                Sorry, your passwords do not match. 
                                Please login again
                                """)
                                self.logged_in = False
                        else: 
                            count += 1
                
                elif next_action == '3':
                    self.user_name = input("Enter new user_name.")
                    
                    
                elif next_action == '4':
                    self.age = input("Enter correct age.")
                    
                elif next_action =='5':
                    self.role = input("Enter current job title.")
                    
                else:
                    print("input not recognized. Try agian.\n")
                    
                    
            
        else:
            print("""
            Welcome, new user!! 
            Please take a few minutes to set up your profile on RobCo usernet.
             Follow the onscreen instructions to activate your new account.
            """)
            User.users.append(self.username)
            self.last_name = input("Enter your last name.")
            self.first_name = input("Enter your first name.")
            self.age = input("Enter your age.")
            self.role = input("Enter your job title.")
            self.password = input("Create a new usernet password.")
            self.setup_check = True
            
                    
                            

user1 = User()

user1.user_login(user1.username)
user1.user_login(user1.username)
print(user1.users)
                
            
        
                    

        
        
