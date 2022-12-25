from turtle import*
import colorsys as cs
speed('fastest')
hideturtle()
bgcolor('black')


for i in range(9):
    pencolor(cs.hsv_to_rgb(i/9,1,1))
    r = 300
    for j in range(40):
        fd(r)
        r -= 4
        right(120)

    penup()
    goto(0,0)
    pendown()
    left(40)

exitonclick()