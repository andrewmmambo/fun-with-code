#################################################################################
# Author: Marima Andrew Mambondiumwe
# Assignment: L2:Using Lists to handle UPC Codes
# Purpose:
# -Learn about an important application of computer science, the UPC code
# -Work on the design of a larger problem
# -Use lists in an application problem


######################################################################
# Acknowledgements:
# Dr Jan Pearce-

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
##################################################################################
import sys
digit = 0


def read_file_contents(filenm):
    '''Assuming that the file called "io_input.txt" exists, open it, get
    all the text into a tuple of strings, one normal order and one reverse order
    Close the file and return the contents'''
    in_str = ""
    open_file = file(filenm, "r")       # use upc-input1.txt
    next_line = open_file.readline()    # read the first line
    while len(next_line) > 0:          # while there is something to read
        in_str = in_str + next_line   # concatenate the string to the normal end
        next_line = open_file.readline()        # read the next line
    open_file.close()
    return (in_str) # returning a tuple





def is_twelve_numbers(input_string):
    """checks whether the inputted digits are exactly 12"""
    while len(str(input_string)) == 12:
        break

    else:
        print("Invalid input")
        sys.exit()


def separate_num(input_string):
    """separates the digits and puts them into a list"""
    ls=[]
    input_string = str(input_string)
    my_list = list(input_string)                                                  # this puts the digits into a list
    for i in my_list:
        ls.append(int(i))
    print("The list of separate digits is," + str(ls))
    return ls


def sum_odd_num(input_string):
    """takes the values of all the odd-numbered digits in the list and sums them up and multiplies the total with 3"""

    counter = 1

    odd = 0

    for i in input_string:
        if counter % 2 == 1:                                              # odd numbers
            odd += int(i)
        counter += 1
        return odd



def sum_even_num(input_string):
    """takes the values of all the even-numbered digits in the list except the last one and sums them up"""
    counter = 1
    evens = 0
    modulo_check = 0
    for i in input_string :
        if(counter% 2 == 0 and counter < 12):#even numbers
            evens += int(i)
        counter += 1
        return evens


def remainder(sen, son):
    """adds the totals evens and total odds and returns the remainder when the total is divided by 10."""
    t1 = sen + son
    mo = t1 % 10
    if mo == 0:
        return mo                                                                   # returns the modulo when it is 0
    else:
        return 10 - mo                                                              # returns 10 minus the modulo,if the modulo is not 0

def convert_to_binary(sn):
    """converts the seperate digits in the list into binary numbers using the dictionary created in this function"""
    d_left = {0: '0001101', 1: '0011001', 2: '0010011', 3: '0111101', 4: '0100011', 5: '0110001', 6: '0101111', 7: '0111011', 8: '0110111', 9: '0001011'}
    d_right = {0: '1110010', 1: '1100110', 2: '1101100', 3: '1000010', 4: '1011100', 5: '1001110', 6: '1010000', 7: '1000100', 8: '1001000', 9: '1110100'}
    list_left = sn[0:6]
    list_right = sn[6:]
    temp_left = []
    temp_right =[]
    for i in list_left:
        temp_left.append(d_left[i])
    print(temp_left)
    for i in list_right:
        temp_right.append(d_right[i])
    print (temp_right)
    new_list = temp_left + temp_right
    fstrn = ""
    for i in new_list:
        fstrn = fstrn + i
    return fstrn

def main():                                                     #this defines the main function
    while True:
        filenm = raw_input("What is the input filename? ")
        if filenm == "upc-input1.txt" or filenm == "upc-input2.txt":
                break
    if filenm == "":
        filenm = "upc-input1.txt"          # use io_input.txt if no filename entered
    input_string = int(read_file_contents(filenm))
    if filenm == "upc-input1.txt":
        print("upc-input1.txt read.")
    else:
        filenm == "upc-input2.txt"
        print("upc-input2.txt read.")
    print("\nHere is the file in the normal order\n")
    print(input_string)
    is_twelve_numbers(input_string)
    sn = separate_num(input_string)
    son = sum_odd_num(sn)
    sen = sum_even_num(sn)
    tn = remainder(sen, son)
    print("The modulo check digit is, " + str(tn))
    if tn == sn[11]:
        pass
    else:
        print("That is not a valid barcode")
        return 0
    bn = convert_to_binary(sn)
    print("The binary numbers are, " + str(bn))




main()                                                  #this calls the main function
