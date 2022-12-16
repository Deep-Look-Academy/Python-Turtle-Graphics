from turtle import*
import colorsys as cs
speed('fastest')
hideturtle()
bgcolor('black')


for i in range(15):
    pencolor(cs.hsv_to_rgb(i/15,1,1))
    r = 140
    for j in range(10):
        circle(r)
        r -= 4
    right(24)

exitonclick()