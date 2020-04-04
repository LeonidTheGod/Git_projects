import tkinter as tk
import sys
import math

alg = "lfrfl"

class Tk_Turtle:
    def __init__(self, canvas, x=0, y=0):
        self.canvas = canvas
        self.angle = 0
        self.x = x
        self.y = y

    def left(self, angle):
        self.angle += angle  
    
    def right(self, angle):
        self.angle -= angle    
    
    def set_angle(self, angle):
        self.angle = angle
    
    def fd(self, length):
        x1 = length * math.cos(math.radians(self.angle))
        y1 = -length * math.sin(math.radians(self.angle))

        self.canvas.create_line(self.x, self.y, self.x + x1, self.y + y1)
        self.x, self.y = self.x + x1, self.y + y1


class Window:
    def __init__(self, root):
        self.root = root
        self.levi_canvas = tk.Canvas(width=1600, height=800, bg="ivory")
        self.r_button = tk.Button(root, text="Random")
        self.r_button.place(x=1300, y = 450)
        self.levi_canvas.pack()
    
    def levi_main(self, n, actions=None, size=None):
        if not actions:
            actions = "f"
        if not size:
            size = 380 / 2 ** (n/2)
        for i in actions:
            if i == "f":
                if n != 0:
                    self.levi_main(n - 1, alg, size)
                else:
                    turtle.fd(size)
            elif i == 'l':
                turtle.left(45)
            elif i == 'r':
                turtle.right(90)

def main():
    global turtle
    root = tk.Tk()
    root.geometry("1400x500")
    window = Window(root)
    turtle = Tk_Turtle(window.levi_canvas, 500, 400)

    window.levi_main(18)
    root.mainloop()

main()