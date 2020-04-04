import tkinter as tk
import math
import random
import time

class Ball:
    def __init__(self, window):
        global balls
        self.window = window
        self.x = 0
        self.y = 0
        self.angle = 0
        self.size = 20
        self.death_count = 5
        # self.gravity = 1
        # self.gravityx = 1/2
        self.id = self.window.basket_canvas.create_oval(-10, -10, -10, -10, fill="red")

    def create_ball(self, x=100, y=400, angle=10, vx=1, vy=1):
        self.vx = vx
        self.vy = vy
        self.window.basket_canvas.coords(self.id, x, y, x+self.size, y+self.size)
        self.x, self.y = map(lambda x: x + self.size/2, self.window.basket_canvas.bbox(self.id)[:2])
    
    def move(self, ball_object):
        self.x += self.vx
        self.y -= self.vy
        self.window.basket_canvas.moveto(self.id, self.x, self.y)

        if self.x + self.size >= self.window.stoprect[2] or self.x <= self.window.stoprect[0]:
            self.vx = -self.vx / 2
            self.x += self.vx*2
            self.death_count -= 1

        if self.y + self.size >= self.window.stoprect[3] or self.y <= self.window.stoprect[1]:
            self.vy = -self.vy / 2
            self.y -= self.vy*2
            self.death_count -= 1

        if not self.death_count:
            print("ball died")
            balls.remove(ball_object)
            self.window.basket_canvas.delete(self.id)

            
        # elif self.count <= 0 and self.count >= -10:
        #     self.vy = 0
        #     self.vx = 0
        #     self.count -= 2
        # else:
        #     self.window.basket_canvas.move(self.id)
        # if self.count > 0:
        #     self.vy -= self.gravity
        # if self.vx > 1:
        #     if self.count != 3:
        #         self.vx -= self.gravityx / 2
        #     else:
        #         self.vx -= self.gravityx / 4
        # self.window.basket_canvas.update()
            


class Window:
    def __init__(self, root):
        self.root = root
        self.stoprect = [10, 10, 1400, 745]
        self.basket_canvas = tk.Canvas(width=1600, height=800, bg="ivory")
        self.r_button = tk.Button(root, text="Create ball", width=15)
        self.r_button.place(x=1410, y = 10)
        self.basket_canvas.pack()
        self.basket_canvas.create_rectangle(*self.stoprect)


class Arrow:
    def __init__(self, window, ball):
        self.window = window
        self.position = [110, 410]
        self.arrow = window.basket_canvas.create_line(*self.position, self.position[0] + 20, self.position[1] - 20, fill='skyblue',
                width=5, arrow=tk.LAST,
                activefill='blue',
                arrowshape="10 17 10")

class ControlManager():
    def __init__(self, root, window, arrow):
        self.window = window
        self.balls = []
        self.arrow = arrow
        self.moving_now = None
        self.size_of_moving_obj = 0

        # window.r_button.bind("<1>", self.ball.create_ball)
        root.bind("<ButtonPress-1>", self.on_start)
        root.bind("<B1-Motion>", self.on_drag)
        root.bind("<ButtonRelease-1>", self.on_drop)

    def on_start(self, event):
        pass

    def on_drag(self, event):
        self.window.basket_canvas.coords(self.arrow.arrow, *self.arrow.position, event.x, event.y)

    def on_drop(self, event):
        b = event.y - self.arrow.position[1]
        c = event.x - self.arrow.position[0]
        print(f"{c} = {event.x} - {self.arrow.position[1]}")
        a = math.sqrt(b**2 + c**2)
        angle = math.degrees(math.asin(b/a))
        vx = c / 100
        vy = -b / 100
        self.window.basket_canvas.coords(self.arrow.arrow, *self.arrow.position, self.arrow.position[0]+20, self.arrow.position[1]-20)
        ball = Ball(self.window)
        balls.append(ball)
        ball.create_ball(angle=angle, vx=vx, vy=vy)
        new_game(balls, self.window)


def new_game(balls, window):
    while balls:
        for ball in balls:
            ball.move(ball)
            window.basket_canvas.update()
    print("no balls")

def main():
    global balls

    root = tk.Tk()
    root.geometry("1500x500")
    # root.wm_state("zoomed")

    balls = []
    window = Window(root)
    ball = Ball(window)
    ball.create_ball(1)
    arrow = Arrow(window, ball)
    ControlManager(root, window, arrow)

    root.mainloop()

main()