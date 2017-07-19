#################################################################################
# Author: Marima Andrew Mambondiumwe
# Assignment: A9: Life Path Numbers
# Purpose: to gain practice in creating and using a fruitful function which employs integer division and modulus.

######################################################################
# Acknowledgements:
#Dr Jan Pearce-peel_digits.py

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
##################################################################################

def peel_digits(num):
    '''given a positive integer num, peel_digits returns a list filled with the digits
    eg. given 1984, peel_digits returns the list [1, 9, 8, 4]'''
    str_num = str(num)  # convert to string to utilize Python's strong string features
    sum = 0  # create empty list
    for letter in str_num:
        sum += int(letter)  # Puts each digits into list
    # print(digit_list)
    return sum              #returns sum

def enter_month_of_birth():             #this function prompts the user to input his month of birth
    """this asks the user to input their month of birth"""
    print ("January       =    1")
    print ("February      =    2")
    print ("March         =    3")
    print ("April         =    4")
    print ("May           =    5")
    print ("June          =    6")
    print ("July          =    7")
    print ("August        =    8")
    print ("September     =    9")
    print ("October       =    10")
    print ("November      =    11")
    print ("December      =    12")
    print('Here is your menu of options Make a corresponding integer choice for your birth month: ')
    is_valid = False
    while is_valid == False:
        month = raw_input("Enter Choice: ")
        month = int(month)
        if((month >0) and (month < 13)):
            is_valid = True
        else:
            is_valid = False
    return(month)

def enter_date_of_month_born(month):                    #this defines the function enter_date_of_month
    """this asks the user to input their month of birth"""

    is_valid = True
    while is_valid == True:
        date = raw_input("Enter the day you were born in (make sure that day is in range [0-31]: ")
        date = int(date)
        if(month==2) and ((date > 0) and (date <= 29)):
            is_valid = False
        elif(month==4 or month==6 or month==9 or month==11) and ((date >0) and (date < 31)):
            is_valid = False
        elif(month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12) and ((date >0) and (date < 32)):
            is_valid = False
        else:
            is_valid = True
    return(date)                #returns the date


def enter_year_of_birth():
    """this asks the user to input the year that they were born"""
    is_valid = False
    while is_valid == False:
        year = raw_input("Enter the year you were born in (make sure that year is in range [1900-2015]: ")
        year = int(year)

        if((year >1899) and (year < 2016)):
            is_valid = True
            year=peel_digits(year)
        else:
            is_valid = False
    return(year)

def num_decider(nom):           #this function determines whether the input from the user is a master number or not
    if nom % 11 == 0:
        return(nom)
    else:
        nom=peel_digits(nom)
        return(nom)             #returns the integer nom

def path_number(mon, date, year):       #this function calculates the pathnumber using the user input
    """this adds the mon,date and year inputs from the user"""
    add=mon + date + year

    while True:                          #the while loop continues calculating the path number until a return is reached.
        if add %11 == 0:
            return(add)
        elif add < 10:
            return(add)
        else:
            add= peel_digits(add)

def meaning_of_pathlife(path_num):
    """this gives the traits and description of each life number"""
    if path_num == 1:
        print("You are a born leader." )
    elif path_num == 2:
        print("The key word in your nature is peacemaker.")
    elif path_num == 3:
        print("You possess a great talent for creativity and self expression. ")
    elif path_num ==4:
        print("You are practical, down to earth with strong ideas about right and wrong. ")
    elif path_num ==5:
        print("The key to your personality is freedom. ")
    elif path_num ==6:
        print("You possess great compassion and seek to be of service to others. ")
    elif path_num ==7:
        print("The searcher and the seeker of the truth. ")
    elif path_num ==8:
        print("You are gifted with natural leadership and the capacity to accumulate great wealth. ")
    elif path_num ==9:
        print("You are the philanthropist, humanitarian, socially conscious. ")
    elif path_num ==11:
        print("The Life Path 11 has the potential to be a source of inspiration and illumination for people. ")
    elif path_num ==22:
        print("You were born under the most powerful and potentially the most successful of all Life Path numbers. ")

    else:
        return path_num



def main():                                     #this defines the main function
    month=enter_month_of_birth()                #this calls the month function in the main
    month = num_decider(month)                  #this converts month into the function num decider

    date=enter_date_of_month_born(month)
    date= num_decider(date)

    year=enter_year_of_birth()
    year=num_decider(year)

    path_num = path_number(month, date, year)
    print("Your path number is " + str(path_num))
    meaning_of_pathlife(path_num)

main()                                          #this calls the main function