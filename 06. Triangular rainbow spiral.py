from turtle import*
import colorsys as cs
speed('fastest')
hideturtle()
bgcolor('black')
width(2)

for i in range(300):
    color(cs.hsv_to_rgb(i/300,1,1))
    left(121)
    fd(i*1.5)

exitonclick()