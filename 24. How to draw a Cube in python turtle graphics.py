from turtle import*
pensize(3)
penup()
goto(-100,-100)
pendown()

for i in range(4):
    forward(200)
    left(90)

left(135)
forward(100)
right(45)
forward(200)
right(135)
forward(100)
backward(100)
left(45)
forward(200)
right(45)
forward(100)

hideturtle()
exitonclick()