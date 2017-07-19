#################################################################################
# Author: Marima Andrew Mambondiumwe
# Assignment: A6 Turtle Houses, Animals, People, etc.
# Purpose: To very simply demonstrate the turtle library to demo shapes. learn to use functions, more about image color in addition to gaining practice with turtle graphics.
######################################################################
# Acknowledgements:
# None--original work

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
##################################################################################
import turtle                   #imports turtle from the library
turtle.colormode(255)           # change color modes
wn=turtle.Screen()              # this creates a screen

def draw_castle_top():
    '''draws the top of the castle'''
    wn.bgcolor("#2DFOFA")               #this changes the screen background color to a RGB color
    ted=turtle.Turtle()                 #this creates a turtle called ted from the Turtle library
    ted.pensize(5)                      #this sets the size of the imprint left by the turtle
    ted.up()
    ted.setpos(-150,150)                #this sets the position of the turtle in the window
    ted.down()

    for i in range(5):                  #a loop for repeating the movement of the turtle
        ted.forward(30)
        ted.right(90)
        ted.forward(30)
        ted.left(90)
        ted.forward(30)
        ted.left(90)
        ted.forward(30)
        ted.right(90)

    ted.forward(30)
    ted.right(90)
    ted.forward(120)
    ted.right(90)
    ted.forward(70)
    ted.left(90)
    ted.forward(250)

    ben=turtle.Turtle()
    ben.color("black")
    ben.pensize(5)
    ben.up()
    ben.setpos(-150,150)
    ben.down()
    ben.fillcolor("coral")          #this sets the color of the area covered by the turtle as it moved
    ben.begin_fill()                #this begins filling in the area covered by the turtle as it moved
    ben.right(90)
    ben.forward(120)
    ben.left(90)
    ben.forward(70)
    ben.right(90)
    ben.forward(250)
    ben.left(90)
    ben.forward(190)
    ben.end_fill()                  #this ends filling in the area covered by the turtle as it moved

def draw_windows():
    '''draws windows of the castle'''
    pat=turtle.Turtle()
    pat.pensize(5)
    pat.color("black")
    pat.shape("classic")            #this sets the shape of the turtle to classic
    pat.up()
    pat.setpos(-100,60)
    pat.down()
    pat.stamp()
    pat.fillcolor("aqua")
    pat.begin_fill()
    pat.circle(15)
    pat.end_fill()

    bat=turtle.Turtle()
    bat.pensize(5)
    bat.color("black")
    bat.shape("classic")
    bat.up()
    bat.setpos(15,60)
    bat.down()
    bat.stamp()                 #this leaves an imprint of the shape of the turtle as it moves
    bat.fillcolor("aqua")
    bat.begin_fill()
    bat.circle(15)              #this makes the turtle draw a circle on the window
    bat.end_fill()

    sam=turtle.Turtle()
    sam.pensize(5)
    sam.color("black")
    sam.shape("classic")
    sam.up()
    sam.setpos(120,60)
    sam.down()
    sam.stamp()
    sam.fillcolor("aqua")
    sam.begin_fill()
    sam.circle(15)
    sam.end_fill()

def castle_name():
    '''this writes the name of the castle on top of the castle'''
    ray=turtle.Turtle()
    ray.shape("turtle")
    ray.color("purple")
    ray.up()
    ray.setpos(0,180)                   #this sets the position where the turtle will begin to write
    ray.down()
    ray.write("King Castle",move=False,align='center',font=("Harlow solid italic",60,("bold","normal")))    #this makes the turtle write something on the window

def main():             #this is the main function
    draw_castle_top()
    draw_windows()
    castle_name()
    wn.exitonclick()     #the window closes when clicked

main()                   # this calls the main function



