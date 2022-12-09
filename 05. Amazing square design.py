from turtle import*
import colorsys as cs
speed('fastest')
hideturtle()
bgcolor('black')
pencolor('red')
for i in range(400):
    color(cs.hsv_to_rgb(i/400,1,1))
    left(91)
    fd(i)
    

exitonclick()