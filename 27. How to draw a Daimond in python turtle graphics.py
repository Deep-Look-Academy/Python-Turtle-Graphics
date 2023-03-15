from turtle import*

penup()
goto(-100,-100)
pendown()
pensize(3)
left(30)

for i in range(2):
    forward(270)
    left(60)
    forward(200)
    left(120)

hideturtle()
exitonclick()