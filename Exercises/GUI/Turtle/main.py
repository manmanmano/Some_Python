from turtle import Turtle, Screen

timmy = Turtle()

for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

for _ in range(20):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()


screen = Screen()
screen.exitonclick()
