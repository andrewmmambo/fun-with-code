# Driver-China Ibuakaeze
# Navigator- Andrew Mambondiumwe
# Usernames-ibuakaezec-mambondiumwea
# T8
# Purpose: Practice breaking larger problems into smaller problems and using strings.



# This function asks the user for his or her name and uses the input of the user to substitute in a story to create a mad lib program."""
def mad_lib():
    """Asks the user for 5 inputs and uses the user's inputs to substitute in a story to create a mad lib program."""
    input1=str(raw_input("What is your name? " ":" ))         # Asks the user for his or her  name.
    input2=str(raw_input("What is your best friend's name? " " :"))
    input3=str(raw_input("Tell us your favorite color: " " "))
    input4=str(raw_input("What is your dream destination, somewhere you have never been before: " " "))
    input5=str(raw_input("In one word describe your how you are feeling now: " " " ))
    
    builder=[input1, input2, input3, input4, input5]   # Puts the user's inputs in a list
    combination="""{0}, you say you want some collabo. {1} needs it badly like a tornado.
    {2}, looks like eminado.I will sing for you in {3}. 
    Until {1} is left asking what {4} wants from the bank!!""".format(builder[0],builder[1],builder[2],builder[3],builder[4])  
    print (combination)
    
    
    
    
    



def main(): 
    """ this invokes the mad_lib function"""
    mad_lib() 
    


main ()     # Calls the main function 