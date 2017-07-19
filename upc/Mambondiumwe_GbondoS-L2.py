#################################################################################
# Authors: Marima Andrew Mambondiumwe and Saffa Gbondo

#   Marima -Driver-Functions and unit tests      Saffa-Navigator-Functions and unit tests
#   Saffa  -Driver-Turtle part                   Marima-Navigator-Turtle part
#   Assignment: L2:Using Lists to handle UPC Codes
#   Purposes:
# -Learn about an important application of computer science, the UPC code
# -Work on the design of a larger problem
# -Use lists in an application problem


######################################################################
# Acknowledgements:
# Dr Jan Pearce-

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################
import turtle                                   # Imports the turtle module

digit = 0
wn = turtle.Screen()                            # creates a turtle window


def read_file_contents(filenm):                 # defines the file read_file_contents
    """opens the files,"upc-input1.txt and upc-input2.txt", get
    all the text into a tuple of strings, one normal order and one reverse order
    Close the file and return the contents"""
    in_str = ""
    open_file = file(filenm, "r")                               # use upc-input1.txt
    next_line = open_file.readline()                            # read the first line
    while len(next_line) > 0:                                   # while there is something to read
        in_str = in_str + next_line                             # concatenate the string to the normal end
        next_line = open_file.readline()                        # read the next line
    open_file.close()
    return (in_str)                                             # returning a tuple


def is_twelve_numbers(input_string):
    """checks whether the inputted digits are exactly 12"""
    while len(str(input_string)) == 12:
        return True
    else:
        print("Invalid input")                                  #  prints invalid input if an invalid input is entered
        guard = turtle.Turtle()                                 #  creates a turtle named guard
        guard.write("Invalid upc code", move=False, align="left", font=("Arial", 20, "normal"))
        guard.hideturtle()
        return False


def separate_num(input_string):
    """separates the digits and puts them into a list"""
    ls = []                                         # this creates an empty list called ls
    input_string = str(input_string)
    my_list = list(input_string)                    # this puts the digits into a list
    for i in my_list:
        ls.append(int(i))                           # appends the characters of the string into a list
    print("The list of separate digits is," + str(ls))
    return ls


def sum_odd_num(input_string):
    """takes the values of all the odd-numbered digits in the list and sums them up and multiplies the total with 3"""

    counter = 1                                     # this initialises the counter to 1 since a computer starts counting at 0

    odd = 0

    for i in input_string:
        if counter % 2 == 1:                        # odd numbered positions
            odd += int(i)                           # it goes through the list and adds all the odd positioned numbers
        counter += 1
    odd = odd * 3                                   # multiplies the sum of the odds by 3
    return odd


def sum_even_num(input_string):
    """takes the values of all the even-numbered digits in the list except the last one and sums them up"""
    counter = 1
    evens = 0
    modulo_check = 0
    for i in input_string:
        if (counter % 2 == 0 and counter < 12):     # even numbered positions
            evens += int(i)                         # it goes through the list and adds all the even positioned numbers
        counter += 1
    return evens


def remainder(sen, son):
    """adds the totals evens and total odds and returns the remainder when the total is divided by 10."""
    t1 = sen + son
    mo = t1 % 10
    if mo == 0:
        return mo                                   # returns the modulo when it is 0
    else:
        return 10 - mo                              # returns 10 minus the modulo,if the modulo is not 0


def convert_to_binary(sn):
    """converts the seperate digits in the list into binary numbers using the dictionary created in this function"""
    d_left = {0: '0001101', 1: '0011001', 2: '0010011', 3: '0111101', 4: '0100011', 5: '0110001', 6: '0101111',   # Creates a dictionary and stores the numbers and their binary number equivalents
              7: '0111011', 8: '0110111', 9: '0001011'}
    d_right = {0: '1110010', 1: '1100110', 2: '1101100', 3: '1000010', 4: '1011100', 5: '1001110', 6: '1010000',
               7: '1000100', 8: '1001000', 9: '1110100'}
    list_left = sn[0:6]        #  splits the upc code into two parts,the left,which is the first 6 digits
    list_right = sn[6:]         # splits the upc code into two parts,the right,which is the last 6 digits
    temp_left = []
    temp_right = []
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


def draw_upc(bn):
    """this draws the upc bar codes using a turtle with the binary numbers,bn"""
    guard = turtle.Turtle()               # this creates the turtle from the turtle library
    for i in bn:
        if i == '0':                       # draws a white vertical line using a turtle for each 0 in the binary number string.

            guard.color('white')            # this changes the color of the turtle to white
            guard.hideturtle()
            guard.pensize(2)
            guard.left(90)
            guard.forward(150)
            guard.forward(-150)
            guard.penup()
            guard.right(90)
            guard.forward(2.75)
            guard.pendown()

        elif i == '1':                      # draws a black vertical line using a turtle for each 1 in the binary number string.

            guard.color('black')
            guard.hideturtle()              # this hides the turtle so that it can not be seen on the window,but it can still draw or leave an imprint as it moves
            guard.pensize(2)
            guard.left(90)
            guard.forward(150)
            guard.forward(-150)
            guard.penup()
            guard.right(90)
            guard.forward(2.75)
            guard.pendown()
        else:
            guard.write("Invalid upc code", move=False, align="left",               # use a turtle to write some text on the window or screen
                        font=("Arial solid italic", 60, ("bold", "normal")))


def upc_test_suite():
    """upc_test_suite() is designed to test the following:
    is_twelve_numbers(input_string)
    separate_num(input_string)
    sum_odd_num(input_string)
    sum_even_num(input_string)
    remainder(sen,son)
    """
    # The following tests the is_twelve_numbers (input_string) function
    testit(is_twelve_numbers("123456789456") == True)
    testit(is_twelve_numbers("883256739659") == True)
    testit(is_twelve_numbers("1234567") == False)

    # The following tests separate_num(input_string) function
    testit(separate_num("12345678") == [1, 2, 3, 4, 5, 6, 7, 8])
    testit(separate_num("123456789456") == [1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 5, 6])
    testit(separate_num("883256739659") == [8, 8, 3, 2, 5, 6, 7, 3, 9, 6, 5, 9])

    # The following tests sum_odd_num(input_string) function
    testit(sum_odd_num([1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 5, 6]) == 30)
    testit(sum_odd_num([2, 2, 8, 4, 5, 6, 10, 8, 9, 4, 3, 7]) == 37)
    testit(sum_odd_num([11, 2, 6, 4, 9, 6, 10, 8, 9, 4, 13, 7]) == 58)

    # The following tests sum_even_num(input_string) function
    testit(sum_even_num([1, 8, 3, 6, 5, 6, 7, 11, 9, 4, 5, 6]) == 35)
    testit(sum_even_num([9, 2, 8, 4, 5, 0, 10, 0, 9, 4, 3, 7]) == 10)
    testit(sum_even_num([11, 15, 6, 3, 9, 6, 10, 8, 9, 4, 13, 7]) == 36)

    # The following tests the remainder(sen,son) function
    testit(check_remainder(20) == True)
    testit(check_remainder(13) == False)
    testit(check_remainder(9) == False)
    testit(check_remainder(30) == True)

    # The following tests the convert_to_binary(sn) function

    testit(convert_to_binary([1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]) == "001100100100110111101010001101100010101111")
    testit(convert_to_binary([7, 8, 9, 1, 2, 3, 1, 2, 3, 4, 5, 6]) == "011101101101110001011001100100100110111101")
    testit(convert_to_binary([3, 2, 4, 3, 6, 2, 3, 2, 7, 3, 4, 1]) == "011110100100110100011011110101011110010011")


def input_strings(upc_code):
    """this writes the upc code below the bar codes using the input string"""
    guard = turtle.Turtle()
    guard.penup()
    guard.setpos(0, -20)
    guard.hideturtle()

    for i in range(0, len(str(upc_code))):
        if i == 1 or i == 6 or i == 11:
            guard.forward(40)  # Larger space
        else:
            guard.forward(10)  # smaller space
        number = str(upc_code)[i]
        guard.write(number, move=False, align="left", font=("Arial solid italic", 10, ("bold", "normal")))              # this prints the upc code below the bar codes


def main():                                                     # this defines the main function
    while True:
        filenm = raw_input("What is the input filename? ")                  # this asks the user to input in a filename
        if filenm == "upc-input1.txt" or filenm == "upc-input2.txt":         # this only allows the user to put in the correct file name,otherwise they will continue to be prompted
            break
    if filenm == "":
        filenm = "upc-input1.txt"                                              # use upc-input1.txt if no filename entered
    input_string = int(read_file_contents(filenm))
    if filenm == "upc-input1.txt":
        print("upc-input1.txt read.")
    else:
        filenm == "upc-input2.txt"
        print("upc-input2.txt read.")
    print("\nHere is the file in the normal order\n")
    print(input_string)
    bool = is_twelve_numbers(input_string)
    if bool is True:                                                            # if the input is correct,then proceed to the next functions
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
        input_strings(input_string)
        draw_upc(bn)

    #upc_test_suite(testit)

    wn.exitonclick()                # this exits the turtle window when it is clicked


main()                              # this calls the main function
