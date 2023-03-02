filename = input("Enter the file you want to analyze.")

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file '" + filename + "' does not exsist."
    print(msg)
    
else:
    #count the approximate number of words in the file.
    words = contents.split()
    numb_words = len(words)
    print("The file  '" + filename + "' has about " + str(numb_words) + " words.")
