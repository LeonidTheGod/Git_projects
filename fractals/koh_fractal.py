import turtle
import sys

sys.setrecursionlimit(2500)
turtle.speed(100)
turtle.penup()
turtle.hideturtle()
turtle.goto(-200, -300)
turtle.left(90)
turtle.pendown()

def koh(n, size):
    if n == 0:
        return

    koh(n - 1, size)
    turtle.right(60)
    turtle.fd(size)

    koh(n - 1, size)
    turtle.left(120)
    turtle.fd(size)

    koh(n - 1, size)
    turtle.right(60)
    turtle.fd(size)

    koh(n - 1, size)


n = 7
try:
    size = 10/n
except:
    size = 5

turtle.fd(size)
koh(n, size=size)

turtle.exitonclick()