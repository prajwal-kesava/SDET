import turtle 
a=turtle.Turtle()
a.color("cyan")
a.speed(0)
def square():
    for side in range(4):
        a.forward(50)
        a.right(90)
        for side in range(4):
            a.forward(50)
            a.left(90)
          

a.penup()
a.forward(100)
a.pendown()

for sq in range(80):
    square()
    a.forward(5)
    a.left(5)

a.hideturtle()    