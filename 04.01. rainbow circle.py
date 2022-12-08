from turtle import*
import colorsys as cs
speed('fastest')
hideturtle()
bgcolor('black')

for i in range(25):
    for j in range(15):
        color(cs.hsv_to_rgb(i/15,j/25,1))
        right(90)
        circle(200-i*4,90)
        left(90)
        circle(200-i*4,90)
        right(180)
        circle(50,24)

exitonclick()