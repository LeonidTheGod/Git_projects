import math
import tkinter as tk
import json
import random

path = "fibonacci.json"
data = json.load(open(path))
all_fib_list = data["list"]

def get_fib_list(length):
    return all_fib_list[:length + 1] 

class Window:
    def __init__(self, root, fib_list, size):

        self.root = root
        self.width_a = 2
        self.spiral_canvas = tk.Canvas(width=1600, height=800, bg="ivory")
        self.r_button = tk.Button(root, text="Random", command=self.random_spiral)
        self.r_button.place(x=1300, y = 450)
        self.spiral_canvas.pack()
        self.create_fib_rects(fib_list, size)
    
    def random_spiral(self):
        self.spiral_canvas.delete(tk.ALL)
        fib_list = [random.randint(1,20) for i in range(15)]
        self.create_fib_rects(fib_list, size, counter=random.randint(0, 3))

    def get_list(self, r, q):
        
        quater_x = [-r, 0, r, 0, -r]
        quater_y = [1, 1, -1, -1]
        list_1 = []

        for x in range(round(quater_x[q]), round(quater_x[q + 1] + quater_y[q]), quater_y[q]):
            y = math.sqrt(r**2 - x**2)*quater_y[q]*(-1)
            list_1.append(x)
            list_1.append(y)
        return(list_1)
    
    def create_fib_rects(self, fib_list, mult, counter=0, y=370, x=760):
        
        mult_list = [[mult, -mult], [mult, mult], [-mult, mult], [-mult, -mult]]
        middle_list = [[mult, 0], [0, mult], [-mult, 0], [0, -mult]]

        for c in fib_list[1::]:
            x1 = x + c * mult_list[counter][0]
            y1 = y + c * mult_list[counter][1]
            # self.spiral_canvas.create_rectangle(x, y, x1, y1, outline = "gray")
            list_1 = self.get_list(mult*c, counter)
            for i in range(0, len(list_1) - 2, 2):
                self.spiral_canvas.create_line(x + list_1[i] + middle_list[counter][0]*c, y + list_1[i+1]+ middle_list[counter][1]*c,
                    x + list_1[i+2] + middle_list[counter][0]*c, y + list_1[i+3]+ middle_list[counter][1]*c, width = self.width_a)
            x, y = x1, y1
            if counter != 3:
                counter += 1
            else:
                counter = 0

class Scrollbar:

    def __init__(self, window, root):
        global size, length
        self.window = window
        self.root = root
        self.tmp_size = size
        self.tmp_length = length
        self.len_controller = 1
        self.len_controller2 = 1

        lowFrame = tk.Frame(self.root)
        lowFrame.place(x=1300, y=300, width=180, height=16)
        self.scrollbar1 = tk.Scrollbar(lowFrame, jump=0, width=16, orient="horizontal")
        self.scrollbar1.pack(side="top", fill=tk.X)        
        self.scrollbar1.config(command=self.change_size)
        self.scrollbar1.set(float(size/1000*15), 0)
        
        lowFrame = tk.Frame(self.root)
        lowFrame.place(x=1300, y=350, width=180, height=16)
        self.scrollbar2 = tk.Scrollbar(lowFrame, jump=0, width=16, orient="horizontal")
        self.scrollbar2.pack(side="top", fill=tk.X)
        self.scrollbar2.config(command=self.change_length)
        self.scrollbar2.set(float(length/1000*55), 0)
      
        lowFrame = tk.Frame(self.root)
        lowFrame.place(x=1300, y=400, width=180, height=16)
        self.scrollbar3 = tk.Scrollbar(lowFrame, jump=0, width=16, orient="horizontal")
        self.scrollbar3.pack(side="top", fill=tk.X)
        self.scrollbar3.config(command=self.change_width)
            
    
    def get_length(self, size):
        i = 0
        while all_fib_list[i] * size < 1000:
            i += 1
        return i - 1

    def change_width(self, a, b):
        global size, length
        self.window.width_a = int(float(b)*1000//55)
        self.scrollbar3.set(float(b), 0)
        self.window.spiral_canvas.delete(tk.ALL)
        if self.tmp_length != 0:
            self.window.create_fib_rects(get_fib_list(self.tmp_length), size)
        else:
            self.window.create_fib_rects(get_fib_list(length), size)


    def change_size(self, a, b):
        global size, length
        size = int(float(b)*1000//15) + 1
        print(length)
        if all_fib_list[length] * size > 1000 and self.len_controller:
            self.tmp_length = length
            self.len_controller = 0
        elif all_fib_list[length] * size > 1000:
            length = self.get_length(size)
            self.window.spiral_canvas.delete(tk.ALL)
            self.window.create_fib_rects(get_fib_list(length), size)
        elif all_fib_list[length] * size < 1000:
            if length < self.tmp_length:
                length += 1
            self.window.spiral_canvas.delete(tk.ALL)
            self.window.create_fib_rects(get_fib_list(length), size)
        self.scrollbar1.set(float(b), 0)
        print(length, self.tmp_length, size)

    def change_length(self, a, b):
        global size, length
        length = int(float(b)*1000//55)

        if all_fib_list[length] * size > 1000 and self.len_controller2:
            self.tmp_length = self.get_length(size)
            self.len_controller2 = 0
            self.window.create_fib_rects(get_fib_list(self.tmp_length), size)
        elif all_fib_list[length] * size < 1000:
            self.tmp_length = 0
            self.len_controller2 = 1
            self.window.spiral_canvas.delete(tk.ALL)
            self.window.create_fib_rects(get_fib_list(length), size)
        self.scrollbar2.set(float(b), 0)
        print(length, self.tmp_length, size)



def main():
    global length, size
    length = 3
    size = 15
    root = tk.Tk()
    root.wm_state('zoomed')
    fib_list = (get_fib_list(length))
    window = Window(root, fib_list, size)
    Scrollbar(window, root)

    root.mainloop()

main()  