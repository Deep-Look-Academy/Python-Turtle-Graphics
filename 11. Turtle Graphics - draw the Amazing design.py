from turtle import*
import colorsys as cs

speed("fastest")
bgcolor("black")
hideturtle()

for i in range(100):
    pencolor(cs.hsv_to_rgb(i/100,.6,1))
    right(i+1)
    circle(170,i)
    fd(i)
    right(90)
    
exitonclick()