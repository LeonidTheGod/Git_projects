import turtle
import sys

sys.setrecursionlimit(2500)
turtle.speed(10)
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
    turtle.right(120)
    koh(n - 1, size)
    turtle.left(120)
    koh(n - 1, size)
    turtle.left(120)
    koh(n - 1, size)    
    turtle.right(120)
    koh(n - 1, size)

n = 3
try:
    size = 50/n
except:
    size = 5

koh(n, size=size)

turtle.exitonclick()