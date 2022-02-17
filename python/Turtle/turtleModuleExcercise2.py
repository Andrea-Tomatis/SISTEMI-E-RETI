'''
Author: Andrea Tomatis

Date: 11/30/2020

control the turtle cursor with keyboard arrows
'''

import turtle

robot = turtle.Turtle()
win = turtle.Screen()


def left():
    if robot.xcor() >= -380:
        robot.setx(robot.xcor() - 10)
    print(f"left {robot.pos()}")

def right():
    if robot.xcor() <= 380:
        robot.setx(robot.xcor() + 10)
    print(f"right {robot.pos()}")

def up():
    if robot.ycor() <= 280:
        robot.sety(robot.ycor() + 10)
    print(f"up {robot.pos()}")

def down():
    if robot.ycor() >= -280:
        robot.sety(robot.ycor() - 10)
    print(f"down {robot.pos()}")


def space():
    robot.reset();
def one():
    robot.pencolor("black")
def two():
    robot.pencolor("red")
def three():
    robot.pencolor("green")
def four():
    robot.pencolor("orange")
def five():
    robot.pencolor("blue")
def penUp():
    robot.up()
def penDown():
    robot.down();

win.setup(width=800,height=600)
win.title(win.textinput("NIM", "Name of the screen:"))
win.bgcolor("white")


win.listen()

win.onkey(left,"Left")
win.onkey(right,"Right")
win.onkey(up,"Up")
win.onkey(down,"Down")
win.onkey(space,"space")

win.onkey(one,"1")
win.onkey(two,"2")
win.onkey(three,"3")
win.onkey(four,"4")
win.onkey(five,"5")

win.onkey(penUp,"u")
win.onkey(penDown,"d")

win.onclick(robot.goto)


win.mainloop()
