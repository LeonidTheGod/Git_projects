import tkinter as tk
import sys
import math
import random

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

class Objects:
    def __init__(self, window):
        self.window = window
        self.circles = []
        self.rects = {}
        self.triangles = []
        self.fivestars = []

    def create_rect(self, event, size=20, x=100, y=100):
        rect = self.window.drop_canvas.create_rectangle(x, y, x+size, y+size, fill="red")
        self.rects[rect] = self.window.drop_canvas.bbox(rect)


class Window:
    def __init__(self, root):
        self.root = root
        self.stoprect = [10, 10, 1400, 745]
        self.drop_canvas = tk.Canvas(width=1600, height=800, bg="ivory")
        self.r_button = tk.Button(root, text="Create rect", width=15)
        self.r_button.place(x=1410, y = 10)
        self.drop_canvas.pack()
        self.drop_canvas.create_rectangle(*self.stoprect)

class ControlManager():
    def __init__(self, root, window, obj):
        self.window = window
        self.obj = obj
        self.moving_now = None
        self.size_of_moving_obj = 0
        self.x_offset = 0
        self.y_offset = 0

        window.r_button.bind("<1>", self.obj.create_rect)
        root.bind("<ButtonPress-1>", self.on_start)
        root.bind("<B1-Motion>", self.on_drag)
        root.bind("<ButtonRelease-1>", self.on_drop)

        root.bind("<Left>", self.tur_go)
        root.bind("<Right>", self.tur_go)
        root.bind("<Up>", self.tur_go)
        root.bind("<Down>", self.tur_go)

    
    def tur_go(self, event):
        if event.keysym == "Left":
            turtle.set_angle(180)
        if event.keysym == "Right":
            turtle.set_angle(0)
        if event.keysym == "Up":
            turtle.set_angle(90) 
        if event.keysym == "Down":
            turtle.set_angle(270)
        turtle.fd(100)

    def on_start(self, event):
        print(self.obj.rects)
        for id_o, diap in self.obj.rects.items():
            if event.x >= diap[0] and event.x <= diap[2]\
                    and event.y >= diap[1] and event.y <= diap[3]:
                self.moving_now = id_o
                self.x_offset = event.x - self.obj.rects[id_o][0]
                self.y_offset = event.y - self.obj.rects[id_o][1]
                self.size_of_moving_obj = diap[2] - diap[0]
                print("gacha!", self.x_offset, self.y_offset)

    def check_collision(self, x, y, size):
        for id_o, diap in self.obj.rects.items():
            if id_o == self.moving_now or\
            x + size < diap[0] or\
            x - size > diap[2] or\
            y + size < diap[1] or\
            y - size > diap[3]:
                continue
            elif x - self.x_offset <= diap[2] and x - self.x_offset > diap[2] - 2:
                return("f_right")
            elif x - self.x_offset + size >= diap[0] and x - self.x_offset + size < diap[0] + 2 :
                return("f_left")
            elif y - self.y_offset <= diap[3] and y - self.y_offset > diap[3] - 2:
                return("f_bot")
            elif y - self.y_offset + size >= diap[1] and y - self.y_offset + size < diap[1] + 2:
                return("f_top")

    def double_wall_collision(self, size, m, x, y):
        
        if x - self.x_offset < self.window.stoprect[0] and\
            y - self.y_offset < self.window.stoprect[1]:
            self.window.drop_canvas.moveto(m, self.window.stoprect[0], self.window.stoprect[1])

        elif x - self.x_offset < self.window.stoprect[0] and\
            y + (size - self.y_offset) > self.window.stoprect[3]:
            self.window.drop_canvas.moveto(m, self.window.stoprect[0], self.window.stoprect[3] - size)

        elif x + (size - self.x_offset) > self.window.stoprect[2] and\
            y - self.y_offset < self.window.stoprect[1]:
            self.window.drop_canvas.moveto(m, self.window.stoprect[2] - size, self.window.stoprect[1])

        elif x + (size - self.x_offset) > self.window.stoprect[2] and\
            y + (size - self.y_offset) > self.window.stoprect[3]:
            self.window.drop_canvas.moveto(m, self.window.stoprect[2] - size, self.window.stoprect[3] - size)

    def on_drag(self, event):
        if self.moving_now != None:
            m = self.moving_now
            m_x, m_y = event.x - self.x_offset, event.y - self.y_offset
            size = self.size_of_moving_obj

            col_flag = self.check_collision(x=event.x, y=event.y, size=size)
            print(col_flag)

            if (event.x - self.x_offset < self.window.stoprect[0] or\
                event.x + (size - self.x_offset) > self.window.stoprect[2])\
                and (event.y - self.y_offset < self.window.stoprect[1] or\
                    event.y + (size - self.y_offset) > self.window.stoprect[3]):
                self.double_wall_collision(size, m, x=event.x, y=event.y)

            elif event.x + (size - self.x_offset)> self.window.stoprect[2]:
                self.window.drop_canvas.moveto(m, self.window.stoprect[2] - size, m_y)
                self.obj.rects[m] = [self.window.stoprect[2] - size, m_y, self.window.stoprect[2], m_y + size]
            elif event.x - self.x_offset < self.window.stoprect[0]:
                self.window.drop_canvas.moveto(m, self.window.stoprect[0], m_y)
                self.obj.rects[m] = [self.window.stoprect[0], m_y, self.window.stoprect[0] + size, m_y + size]
            elif event.y - self.y_offset < self.window.stoprect[1]:
                self.window.drop_canvas.moveto(m, m_x, self.window.stoprect[1])
                self.obj.rects[m] = [m_x, self.window.stoprect[1], m_x + size, self.window.stoprect[1] + size]
            elif event.y + (size - self.y_offset) > self.window.stoprect[3]:
                self.window.drop_canvas.moveto(m, m_x, self.window.stoprect[3] - size)
                self.obj.rects[m] = [m_x, self.window.stoprect[3] - size, m_x + size, self.window.stoprect[3]]
            else:
                self.window.drop_canvas.moveto(m, m_x, m_y)
                self.obj.rects[m] = [m_x, m_y, m_x + size, m_y + size]

    def on_drop(self, event):
        self.moving_now = None

def main():
    global turtle
    root = tk.Tk()
    root.geometry("1500x500")
    # root.wm_state("zoomed")
    window = Window(root)
    obj = Objects(window)
    turtle = Tk_Turtle(window.drop_canvas, 500, 400)
    control = ControlManager(root, window, obj)

    root.mainloop()

main()