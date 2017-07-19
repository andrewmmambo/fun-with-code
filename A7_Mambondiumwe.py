#################################################################################
# Author: Marima Andrew Mambondiumwe
# Assignment: A7: Cityscape
# Purpose:To create one or more python functions and use them to create a cityscape or other landscape like a forest or mountain range or beach using turtle graphics
######################################################################
# Acknowledgements:
#Dr Jan Pearce-my street
#A6-Mambondiumwe

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
##################################################################################

import turtle                   #imports turtle from the library
import random                   #imports random from the library
turtle.colormode(255)           # change color modes
wn=turtle.Screen()              # this creates a screen
wn.bgcolor("lime")              # this changes the screen background to a RGB COLOR.

def draw_roof_top():
    """draws the top of the house"""
    sa=turtle.Turtle()                 #this creates a turtle called sa from the Turtle library

    for i in range(3):                  #this for loop randomly picks a color for the roof top from three choices
        fillcolor=random.choice(['orange','blue','aqua'])

        if (fillcolor=='orange'):
            sa.fillcolor('orange')
        elif (fillcolor=='blue'):
            sa.fillcolor('blue')

        else:
            sa.fillcolor('aqua')

    sa.pensize(5)                      #this sets the size of the imprint left by the turtle
    sa.pencolor("orange")
    sa.up()
    sa.setpos(-250,200)                #this sets the position of the turtle in the window
    sa.down()
    sa.begin_fill()
    sa.left(30)
    sa.forward(50)
    sa.right(30)
    sa.forward(70)
    sa.right(30)
    sa.forward(50)
    sa.right(150)
    sa.forward(155)
    sa.end_fill()
    sa.up()
    sa.setpos(100,200)
    sa.down()
    sa.begin_fill()
    sa.right(150)
    sa.forward(50)
    sa.right(30)
    sa.forward(70)
    sa.right(30)
    sa.forward(50)
    sa.right(150)
    sa.forward(155)
    sa.end_fill()
    return

def make_house():
    """this functions draws the rest of the house apart from the roof"""
    sas=turtle.Turtle()
    sas.pensize(5)
    sas.pencolor("brown")
    sas.up()
    sas.setpos(-230,200)                #this sets the position of the turtle in the window
    sas.down()
    sas.fillcolor("brown")
    sas.begin_fill()
    sas.right(90)

    for i in range(4):                  #this for loop draws a square
        sas.forward(120)
        sas.left(90)

    sas.end_fill()
    sas.up()
    sas.setpos(240,200)
    sas.down()
    sas.begin_fill()
    sas.right(90)

    for i in range(4):                  #this for loop draws a square
        sas.forward(120)
        sas.left(90)

    sas.end_fill()

    return

def make_window():
    """this function draws windows to the house"""
    sas=turtle.Turtle()
    sas.pensize(5)
    sas.color("black")
    sas.shape("classic")            #this sets the shape of the turtle to classic
    sas.up()
    sas.setpos(-200,150)
    sas.down()
    sas.stamp()
    sas.fillcolor("white")
    sas.begin_fill()
    sas.circle(12)
    sas.end_fill()

    sas.up()
    sas.setpos(200,150)
    sas.down()
    sas.stamp()
    sas.fillcolor("white")
    sas.begin_fill()
    sas.circle(12)
    sas.end_fill()
    return

def draw_east_street():
    """this functions draws a street going to the east"""
    rat=turtle.Turtle()
    rat.pencolor("aqua")
    rat.up()
    rat.setpos(0,60)
    rat.down()
    rat.pensize(30)
    rat.forward(400)
    rat.backward(800)
    rat.up()
    return

def draw_north_street():
    """this functions draws a street going to the north"""
    sas=turtle.Turtle()
    sas.pencolor("aqua")
    sas.up()
    sas.setpos(0,0)
    sas.down()
    sas.pensize(30)
    sas.left(90)
    sas.forward(400)
    sas.backward(800)
    sas.up()
    return

def write_it():
    """this writes on the window"""
    gib=turtle.Turtle()
    gib.up()
    gib.setpos(0,40)
    gib.down()
    gib.pencolor("blue")
    gib.write("Great Neighbourhood",move=False,align='center',font=("Harlow solid italic",30,("bold","normal")))
    return

def main():
    """ This is the main function """
    draw_roof_top()
    make_house()
    make_window()
    draw_east_street()
    draw_north_street()
    write_it()


    wn.exitonclick()  # wait for a user click on the canvas

main()                 #this calls the main function



