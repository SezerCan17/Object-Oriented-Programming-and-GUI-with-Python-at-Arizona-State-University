from turtle import *

# for turtle shape
shape("turtle")

def makeSquare():
    color('red', 'yellow')  # set fill and outline colors
    begin_fill()
    for i in range(4):  # make a square
        pensize(4)
        forward(100)
        left(90)
    end_fill()

def makeSquare2():
    for i in range(4):  # make another square without filling
        pensize(4)
        forward(100)
        left(90)

def spiral():
    pensize(2)  # set pen size for spiral
    for i in range(18):
        makeSquare2()
        left(20)  # rotate by 20 degrees for spiral effect

def line():
    pencolor('blue')  # set line color to blue
    forward(200)

def cir():
    pencolor('green')  # set circle color to green
    circle(60)

# Drawing functions
makeSquare()  # draw the filled square
penup()
setposition(-200, 0)  # move to a different position
pendown()
spiral()  # draw the spiral
penup()
setposition(0, 200)  # move to a new position
pendown()
line()  # draw the line
penup()
setposition(0, -200)  # move to a new position
pendown()
cir()  # draw the circle

done()
