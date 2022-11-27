from turtle import*
speed(0)
bgcolor('white')
pensize(5)
pencolor('seagreen')


goto(0,0)


goto(200,-120)
pendown()
begin_fill()
color('seagreen')


seth(90)
fd(240)

seth(180)
fd(400)

seth(270)
fd(240)

seth(360)
fd(400)

end_fill()


goto(0,0)
pencolor('red')

seth(180)
fd(20)
seth(90)
fd(80)
seth(180)
begin_fill()
color('red')
circle(80)
end_fill()

up()
goto(-90,-150)
write("Love You Bangladesh",font=16)
goto(0,0)


exitonclick()
