#fm = 'pi_digits.txt'



def print_pi(filename, digits):
    """A quick funtion to print upto a million digits of pi"""
    pi_string =''
    with open(filename) as file_object:
        lines = file_object.readlines()
        for line in lines:
            pi_string += line.strip()
            
    print(pi_string[:digits] + '...')
    print(len(pi_string))
    

def birthday_pi(filename, birthday=120372):
    birthday = input("Enter your birthday in mmddyy format with no slashes.")
    pi_string = ''
    with open(filename) as file_object:
        lines = file_object.readlines()
        for line in lines:
            pi_string += line.strip()
            
    if birthday in pi_string:
        print("Your birthday appears in the first million digits of pi!")
    else:
        print("Your birthday does not appear in the first million digits of pi.")


#print_pi('pi_digits.txt', 55)
birthday_pi('pi_digits.txt')


    
