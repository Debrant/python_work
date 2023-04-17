def count_words(filename):
    """Count the approximate number of words in a file."""
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
        print("The file  '" + filename + "' has about " + str(numb_words) +    
            " words.")
    
# filename = input("Enter the file you want to analyze.")
# count_words(filename) 
filenames = ['alice.txt', 'programming.txt', 'sample.txt', 'swords.txt', 'swords2.txt']
for filename in filenames:
    count_words(filename) 
