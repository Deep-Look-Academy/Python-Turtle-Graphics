from turtle import*
import random

speed("fastest")
pensize(2)
left(90)
backward(100)

colors = [ "red" , "green" , "yellow", "blue"]

def drawTree(l):
    if(l<10):
        return
    else:
        forward(l)
        color(colors[random.randint(0,3)])
        circle(2)
        color('black')
        left(30)
        drawTree(3*l/4)

        right(60)
        drawTree(3*l/4)
        left(30)
        backward(l)

drawTree(100)

right(90)
fd(50)
backward(100)

exitonclick()