from turtle import*
import colorsys as cs
speed('fastest')
hideturtle()
bgcolor('black')
# loop for printing tangent circles
h = 0.8
for i in range(160):
    color(cs.hsv_to_rgb(h,1,1))
    h += .016
    circle( i)
    left(10)
exitonclick()