from turtle import*
import colorsys as cs
speed("fastest")
bgcolor("black")
h = .1
pensize(5)

for j in range(300):
    for i in range(4):
        fillcolor(cs.hsv_to_rgb(h,1,1))
        h+= 0.004
        begin_fill()

        fd(50)
        right(20)
        fd(40)
        right(9)
        end_fill()

    goto(0 , 0)
    right(10)

exitonclick()

    