'''

Author: Andrea Tomatis

date: 20 november 2020

This algorithm draws a regular shape of N sides
'''

from turtle import *  #import the module turtle

#this function draw the shape
def drawShape(angle): 
    color('black', 'black')
    begin_fill()  #start the color filling
    while True:
        forward(50) #go forward of 50px
        left(angle)  #rotate the angle
        if abs(pos()) < 1:  #if the shape is end it stop end the while loop
            break
    end_fill()  #end color filling
    done() #end the draw


def main():
    nSide = int(input("insert the number of side: "))
    drawShape(360/nSide)

    '''
    to draw the shape it divides 360 by the number of side.
    We do this because in a regular shape the sum of eache extern edge
    is equal to 360. 
    '''


if __name__ == "__main__":
    main()
