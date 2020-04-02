import turtle
import sys

sys.setrecursionlimit(2500)
turtle.speed("fastest")
turtle.penup()
turtle.bgcolor("black")
turtle.color("red")
turtle.width(2)
turtle.hideturtle()
turtle.goto(0, -300)
turtle.left(90)
turtle.pendown()

def koh(n, size):
    if n == 0:
        turtle.fd(size)
        return    

    koh(n - 1, size)
    turtle.right(60)
    koh(n - 1, size)
    turtle.left(120)
    koh(n - 1, size)
    turtle.right(60)
    koh(n - 1, size)


n = 5
try:
    size = 30/(n*2)
except:
    size = 5
for i in range(3):
    koh(n, size=size)
    turtle.left(120)

turtle.exitonclick()