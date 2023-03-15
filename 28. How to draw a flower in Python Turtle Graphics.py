from turtle import*

speed("fastest")
pensize(3)

for i in range(8):
    for j in range(5):
        left(72)
        forward(100)
    left(45)

hideturtle()
exitonclick()