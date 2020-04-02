import turtle
import sys

sys.setrecursionlimit(2500)
turtle.speed(100)
turtle.penup()
# turtle.hideturtle()
turtle.goto(-200, -300)
turtle.left(90)
turtle.pendown()

def koh(n, size):
    if n == 0:
        turtle.fd(size)
        return

    koh(n - 1, size)
    turtle.right(90)
    koh(n - 1, size)
    turtle.left(90)
    koh(n - 1, size)
    turtle.left(90)
    koh(n - 1, size) 
    turtle.right(90)
    koh(n - 1, size)

n = 5
try:
    size = 30/(n*1.5)
except:
    size = 7

koh(n, size=size)

turtle.exitonclick()