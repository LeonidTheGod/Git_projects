import math
import tkinter as tk

def get_fib_list(length):
    first, second = 0, 1
    fib_list = [first, second]
    for _ in range(length - 2):
        first, second = second, first
        second = first + second
        fib_list.append(second)
    return fib_list

class Window:
    def __init__(self):
        self.root = tk.Tk()
        self.root.wm_state('zoomed')

        self.spiral_canvas = tk.Canvas(width=1600, height=800, bg="ivory")
        self.spiral_canvas.pack()

    def get_list(self, r, q):
        
        quater_x = [-r, 0, r, 0, -r]
        quater_y = [1, 1, -1, -1]
        list_1 = []

        for x in range(round(quater_x[q]), round(quater_x[q + 1] + quater_y[q]), quater_y[q]):
            y = math.sqrt(r**2 - x**2)*quater_y[q]*(-1)
            list_1.append(x)
            list_1.append(y)
        return(list_1)
    
    def create_fib_rects(self, fib_list, mult=20):
        counter = 0
        y = 370
        x = 760
        mult_list = [[mult, -mult], [mult, mult], [-mult, mult], [-mult, -mult]]
        middle_list = [[mult, 0], [0, mult], [-mult, 0], [0, -mult]]
        for c in fib_list[1::]:
            x1 = x + c * mult_list[counter][0]
            y1 = y + c * mult_list[counter][1]
            self.spiral_canvas.create_rectangle(x, y, x1, y1, outline = "gray")
            list_1 = self.get_list(mult*c, counter)
            for i in range(0, len(list_1) - 2, 2):
                self.spiral_canvas.create_line(x + list_1[i] + middle_list[counter][0]*c, y + list_1[i+1]+ middle_list[counter][1]*c,
                    x + list_1[i+2] + middle_list[counter][0]*c, y + list_1[i+3]+ middle_list[counter][1]*c, width = 2)
            x, y = x1, y1
            if counter != 3:
                counter += 1
            else:
                counter = 0
        

def main():
    fib_conf = (13, 20)
    fib_list = (get_fib_list(fib_conf[0]))
    window = Window()
    window.create_fib_rects(fib_list, fib_conf[1])

    window.root.mainloop()

main()  