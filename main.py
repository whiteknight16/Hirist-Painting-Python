import turtle
from turtle import Turtle,Screen
from random import choice

import colorgram
colors = colorgram.extract("./hirst_painting.webp",30)
color_list=[]
for color in colors:
    r=color.rgb.r
    g=color.rgb.g
    b=color.rgb.b
    color_tuple=(r,g,b)
    color_list.append(color_tuple)


turtle.colormode(255)


t=Turtle()
# Drawing Painting
t.pu()
t.setheading(200)
t.fd(300)
t.setheading(0)
def draw_painting(row,col):
    for i in range(row):
        for j in range(col):
            t.pd()
            t.dot(20,choice(color_list))
            t.pu()
            t.fd(50)
        t.seth(90)
        t.fd(50)
        t.seth(180)
        t.fd(50*col)
        t.seth(360)

draw_painting(5,5)

screen=Screen()
screen.exitonclick()
