import turtle as t
a=t.Turtle()
a.color("black")
for side in range(9):
    a.forward(10*side)
    a.right(360/3)

a.hideturtle()    