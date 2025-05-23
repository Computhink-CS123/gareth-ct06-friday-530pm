import turtle
window=turtle.Screen()
window.setup(width=400,height=400)
skibidi= turtle.Turtle()
skibidi.speed(100)
skibidi.shape("turtle")
skibidi.goto(0,0)
skibidi.up()
while skibidi.xcor() < 190:
    skibidi.forward(1)

skibidi.down()
skibidi.seth(90)

while skibidi.ycor() < 190:
    skibidi.forward(1)

skibidi.seth(180)

while skibidi.xcor() > -190:
    skibidi.forward(1)

skibidi.seth(270)
while skibidi.ycor() > -190:
    skibidi.forward(1)

skibidi.seth(0)
while skibidi.xcor() < 190:
    skibidi.forward(1)
skibidi.seth(90)
while skibidi.ycor() < 0:
    skibidi.forward(1)
window.mainloop()
