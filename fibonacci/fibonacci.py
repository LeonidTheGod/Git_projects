import math
import tkinter as tk
import json

path = "D:\\Progs - Python\\Different\\fibonacci\\fibonacci.json"
data = json.load(open(path))
all_fib_list = data["list"]

def get_fib_list(length):
    list_1 = all_fib_list[:length + 1]
    return list_1

class Window:
    def __init__(self, root, fib_list, size):

        self.spiral_canvas = tk.Canvas(width=1600, height=800, bg="ivory")
        self.spiral_canvas.pack()
        self.create_fib_rects(fib_list, size) 

    def get_list(self, r, q):
        
        quater_x = [-r, 0, r, 0, -r]
        quater_y = [1, 1, -1, -1]
        list_1 = []

        for x in range(round(quater_x[q]), round(quater_x[q + 1] + quater_y[q]), quater_y[q]):
            y = math.sqrt(r**2 - x**2)*quater_y[q]*(-1)
            list_1.append(x)
            list_1.append(y)
        return(list_1)
    
    def create_fib_rects(self, fib_list, mult):
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

class Scrollbar:

    def __init__(self, window, root):
        global size, length
        self.window = window
        self.root = root
        self.tmp_size = size
        self.tmp_length = length

        lowFrame = tk.Frame(self.root)
        lowFrame.place(x=1300, y=300, width=150, height=20)
        self.scrollbar1 = tk.Scrollbar(lowFrame, jump=0, width=16, orient="horizontal")
        self.scrollbar1.pack(side="top", fill=tk.X)        
        self.scrollbar1.config(command=self.change_size)
        self.scrollbar1.set(float(size/1000*20), 0)
        
        lowFrame = tk.Frame(self.root)
        lowFrame.place(x=1300, y=400, width=150, height=20)
        self.scrollbar2 = tk.Scrollbar(lowFrame, jump=0, width=16, orient="horizontal")
        self.scrollbar2.pack(side="top", fill=tk.X)
        self.scrollbar2.config(command=self.change_number)
            
        self.scrollbar2.set(float(length/1000*55), 0)

    def get_size_or_length(self, s_o_l, length, size):
        print("your in f")
        norme = 1000
        if s_o_l == "s":
            if all_fib_list[length] * size <= norme:
                return size
            else:
                size = 0
                while all_fib_list[length] * size <= norme:
                    size += 1
                print("changeeeeeeeeeed", length, size)
                return size
        elif s_o_l == "l":
            if all_fib_list[length] * size <= norme:
                return length
            else:
                length = 2
                while all_fib_list[length] * size <= norme:
                    length += 1
                print("changeeeeeeeeeed", length, size)
                return length


    def change_size(self, a, b):
        global size, length
        size = int(float(b)*1000//20) + 1
    
        length = self.get_size_or_length("l", length, size)
        print(length, size)
        self.scrollbar1.set(float(b), 0)
        self.window.spiral_canvas.delete(tk.ALL)
        self.window.create_fib_rects(all_fib_list[:length + 1], size)

    def change_number(self, a, b):
        global size, length
        length = int(float(b)*1000//55)

        size = self.get_size_or_length("s", length, size)
        print(length, size)
        self.scrollbar2.set(float(b), 0)
        self.window.spiral_canvas.delete(tk.ALL)
        self.window.create_fib_rects(all_fib_list[:length + 1], size)



def main():
    global length, size
    length = 3
    size = 15
    root = tk.Tk()
    # root.wm_state('zoomed')
    root.geometry("1500x500")
    fib_list = (get_fib_list(length))
    window = Window(root, fib_list, size)
    Scrollbar(window, root)

    root.mainloop()

main()  