from turtle import*
import colorsys as cs
speed("fastest")
bgcolor('black')
h = .1
pensize(2)

for i in range(160):
    color(cs.hsv_to_rgb(h,1,1))
    pencolor('black')
    h += 0.04
    begin_fill()
    circle(160-i,100)
    left(90)
    circle(160- i, 100)
    end_fill()

exitonclick()