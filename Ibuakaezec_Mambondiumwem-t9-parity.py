######################################################################
# Driver-Marima A mambondiumwe
# Navigator-China Ibuakaeze
# Purpose: To use test driven development to demonstrate string functions
# and learn some things about binary.
#
######################################################################
# Acknowledgements:
# Modified from original code written by Dr. Jan Pearce
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
######################################################################

import sys


def testit(did_pass):                                                                   #this defines the function testit(did_pass)
    """ Print the result of a test. """
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)


def is_binary(bitstring):                                                               #this defines the function is_binary(bitstring)
    """This function takes a bitstring as input,
    returning True if it is at least 7-bits and consists solely of 0s and 1s
    and returning False otherwise
    Hint: You might use the len() function compared to the sum the 0s and 1s"""
    if len(bitstring) >= 7:                                                             #this if statement will only return true is the input has at least 7 characters which are either ones and zeros.
        for s in bitstring:
            if s == "0" or s == "1":
                pass
            else:
                return False
        return True
    else:
        return False


def is_div_by_sevens(bitstring):                                                            #this defines the function is_div_by sevens(bitstring)
    """This function takes a bitstring as input,
    returning True if the length of the string is evenly divisible by 7
    and returning False otherwise.
    Hint: use the % modulus operator"""
    if len(bitstring) % 7 == 0:                                                             #this checks if the input is evenly divisible by 7
        return True
    else:
        return False


def split_into_sevens(bitstring):                                                           #this defines the function split_into_sevens(bitstring)
    """This function takes a bitstring whose length is evenly divisible by 7 as input,
    It returns the resultant list of 7-bit long strings as output.
    Hint 1: divide the length of your bitstring by 7, converting the result to an integer.
    Loop that many times and use slicing to "chunk" the string
    Hint 2: The list append method will also be useful."""

    list_of_chunks = []                                                                     #this breaks up the input into chunks of 7 apiece.
    for i in range(0, len(bitstring), 7):
        list_of_chunks.append(bitstring[i:i + 7])
    return list_of_chunks


def add_parity(list_of_chunks):                                                             #this defines the function add_parity(list_of_chunks)
    """This function takes a list of binary strings as input, each 7 bits long,
    Using even parity, this function prepends a parity bit at the front end of each string,
    and returns the resulting list of 8-bit binary strings."""

                                                                                            # This function is already correct and tested

    parity_chunks = []
    for byte in list_of_chunks:                                                              # for each 7-bit chunk of binary
        count1s = 0                                                                          # count the 1's
        for letter in byte:
            count1s = count1s+int(letter)
        parity_chunks.append(str(count1s%2)+byte)                                           #count1s%2 is 0 when count1s is even and 1 when count1s is odd
    # print(parity_chunks) # for debugging
    return parity_chunks


def run_all(bitstring):                                                                     #this defines the function run_all(bitstring)
    """This function takes bitstring as input,
    if bitstring is only 0s and 1s with length evenly divisible by 7
    it uses even parity to return the resulting list of 8-bit binary strings.
    otherwise it returns "Input Error" """

                                                                                            # This function is already correct and tested

    if is_binary(bitstring) and is_div_by_sevens(bitstring):
        my_list = split_into_sevens(bitstring)
        return add_parity(my_list)
    else:
        return "Input Error"


def parity_test_suite():                                                                    #this defines the function parity_test_suite
    """Designed to test the following functions:
    is_binary(bitstring)
    is_div_by_sevens(bitstring)
    split_into_sevens(bitstring)
    add_parity(list_of_chunks)
    run_all(bitstring)
    """

    # tests for is_binary()
    testit(is_binary('1001010') == True)
    testit(is_binary('100 1010') == False)
    testit(is_binary('100') == False)

    # tests for is_div_by_sevens(bitstring)
    testit(is_div_by_sevens('1001010') == True)
    testit(is_div_by_sevens('100100011010010100001') == True)
    testit(is_div_by_sevens('1001') == False)
    testit(is_div_by_sevens('10010001101001010001') == False)
    testit(is_div_by_sevens('1001000110100101000110') == False)                                   #additional unit test that i added.
    testit (is_div_by_sevens('01010101010101') == True)                                          #additional  unit test that i added

    #tests for split_into_sevens(bitstring)
    testit(split_into_sevens('1001010') == ['1001010'])
    testit(split_into_sevens('100100011010010100001') == ['1001000', '1101001', '0100001'])
    testit(split_into_sevens('1110011') == ['1110011'])                                           #additional unit test that i added.
    testit(split_into_sevens('11100111110011') == ['1110011', '1110011'])                     #additional unit test that i added.

    #tests for add_parity(list_of_chunks)
    testit(add_parity('') == [])
    testit(add_parity(['1001010']) == ['11001010'])
    testit(add_parity(['1001000', '1101001', '0100001']) == ['01001000', '01101001', '00100001'])
    testit(add_parity(['1001001']) == ['11001001'])                                             #additional unit test that i added


    #tests for run_all(bitstring)
    testit(run_all('1001010') == ['11001010'])
    testit(run_all('100100011010010100001') == ['01001000','01101001','00100001'])
    testit(run_all('10010') == 'Input Error')
    testit(run_all('011') == 'Input Error')                                                       #additional unit test that i added.


def main():                                                                                     #this defines the main function
    """The main() function--used to call all other functions"""
    my_bits=raw_input("Please enter a bitstring with length evenly divisible by 7: ")
    bitstring =is_binary(my_bits)
    print(bitstring)
    divisible_by_7=is_div_by_sevens(my_bits)
    print(divisible_by_7)
    split_into_sevens(my_bits)
    print(split_into_sevens(my_bits))
    parity_test_suite()


main()                                                                                          # calls the main() function


