from turtle import*
import colorsys as cs
speed('fastest')
hideturtle()
bgcolor('black')

for i in range(10):
    pencolor(cs.hsv_to_rgb(i/10,1,1))
    r = 220
    for j in range(40):
        fd(r)
        left(90)
        r -= 4

    penup()
    goto(0,0)
    pendown()
    right(36)

exitonclick()