######################################################################
# Modified by: Marima Andrew Mambondiumwe ******
# username: mambondiumwem

# Assignment: L3 ppm
# Purpose: to learn more about Image ppm files
#   Modified from code written by Dr. Jan Pearce
#   Original code downloaded from:
#   http://cs.berea.edu/csc226/tasks/yourusername-L3-ppm.py and
#   http://cs.berea.edu/csc226/tasks/ppm.py
######################################################################
# Acknowledgements:
# Ben Stephenson: http://pages.cpsc.ucalgary.ca/~jacobs/Courses/cpsc217/W10/code/Topic7/ppm.py
# working from a class: http://bytes.com/topic/python/answers/520360-trouble-displaying-image-tkinter

######################################################################

import time                                                             # imports the time library
from ppm import *                                                       # imports from ppm.py
# Be sure you work with a single ppm object at a time


def main():                                                             # this defines the main function

    wn = PPM_set_up()                                                   # To use the PPM class, this must appear at the beginning of your program: send to the initialzer.

    print("\nWelcome to the PPM introduction!\n")

    ppmdefault=PPM(wn)                                                  # uses default file
    ppmdefault.PPM_display()                                            # this displays the default file
    print("---")

    filename = raw_input("Please input name of PPM-P3 file: ")          # this prompts the user to input the file name
    ppmobject = PPM(wn, filename)

    multipleactions = 'yes'                                             # Creates a variable which allows multiple taks to be done of the PPM file
    while multipleactions == 'yes':                                     # this repaets the code in the while loop if the user inputs yes

        print("Press [1] To turn image red")                            # gives you choices on what actions to do on the image
        print("Press [2] To turn image grey scale")
        print("Press [3] To flip image Horizontal")
        print("Press [4] To rotate image clockwise")
        print("Press [5] To zoom image")
        print("Press [6] To turn Image to a Negative")
        imageaction = raw_input('''Please select an action to be done to the PPM image from the above choices?\n''') # prompts the user to make one selection

        if imageaction == '1':
            ppmobject.PPM_make_red()                      # calls the function from ppm if the condition above is met

        elif imageaction == '2':
            ppmobject.PPM_greyscale()                     # calls the function from ppm if the condition above is met

        elif imageaction == '3':
            ppmobject.PPM_flip_horizontal()               # calls the function from ppm if the condition above is met

        elif imageaction == '4':
            ppmobject.PPM_rotateclockwise()               # calls the function from ppm if the condition above is met

        elif imageaction == '5':
            size = raw_input("By how much would you like to Zoom the Image?, Please enter a number :\n ")   # asks the user for a zoom value
            ppmobject.zoom_PPM(size)                      # calls the function from ppm if the condition above is met

        elif imageaction == '6':
            ppmobject.PPM_negative()                      # calls the function from ppm if the condition above is met

        multipleactions = raw_input('Would you like to apply another action to the Image, yes or  no?:\n ')  # Determines whether the user wants to add more file or not
    ppmobject.PPM_display()                                # this displays the PPM file

    print("---")

    ppmtestlist=PPM(wn)                                     # uses default file
    # The following is a very small image list which differs from the default image
    testlist = [[[0, 0, 255], [0, 255, 0], [0, 30, 30]],[[40, 40, 40], [50, 50, 50],[60, 60, 60]]]
    ppmtestlist.PPM_updatefrompixellist(testlist, "very_small.ppm")
    ppmtestlist.PPM_display()                               # this displays the testlist

    print("\nClick the Quit button to exit all files.")

    PPM_render(wn)                                          # needed to render all of the images you have instantiated

main()                                                      # this calls the main function
