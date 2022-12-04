from turtle import*
pensize(2)
hideturtle()
speed('fastest')
bgcolor('black')
colors =  ['red', 'purple', 'blue', 'green', 'orange', 'yellow'] 


for l in range(250):
    color(colors[l%len(colors)])
    forward(l)
    left(61)

exitonclick()