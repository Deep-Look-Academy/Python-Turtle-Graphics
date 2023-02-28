from turtle import*
speed("fastest")
bgcolor("black")
a = 0
b = 0
pencolor("red")
penup()
goto(0,200)
pendown()
while True:
    forward(a)
    right(b)
    a += 2
    b += 1
    if b == 210:
        break
exitonclick()