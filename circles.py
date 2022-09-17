from turtle import *

def circles(number, radius,radius2):
    angle=360/number
    n=0
    while n<number:
        penup()
        forward(radius)
        pendown()
        circle(radius2)
        penup()
        back(radius)
        left(angle)
        n=n+1

speed(0)
circles(8,10,75)
input()