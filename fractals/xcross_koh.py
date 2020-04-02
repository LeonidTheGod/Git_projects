import turtle
import sys

sys.setrecursionlimit(2500)


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

n = 4
try:
    size = 50/(n*2)
except:
    size = 20

turtle.speed(100)
turtle.penup()
turtle.width(4)
turtle.goto(-300, -300)
turtle.left(90)
turtle.pendown()

for i in range(4):
    koh(n, size=size)
    turtle.right(90)

turtle.exitonclick()