import os
import inspect
import sys
import copy
import json
import tkinter as tk

from PIL import ImageTk, Image
from infos import *

def get_script_dir(follow_symlinks=True):
    if getattr(sys, 'frozen', False):
        path = os.path.abspath(sys.executable)
    else:
        path = inspect.getabsfile(get_script_dir)
    if follow_symlinks:
        path = os.path.realpath(path)
    return os.path.dirname(path)

WIDTH = 1400
HEIGHT = round(WIDTH/3.6)

path = get_script_dir()+'\\'
path_to_json = get_script_dir()+"\\chords.json"

data = json.load(open(path_to_json, encoding="utf8"))

def save_chords_data(chord_name, chord):

    data['All chords'][chord_name] = chord
    with open(path_to_json, "w", encoding='utf8') as file:
        json.dump(data, file, indent=2, ensure_ascii=False)


class Window:
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.wm_state('zoomed')
        self.chord_canv = tk.Canvas(width=290, height=390, bg='ivory')
        self.chord_canv.place(x=400, y=350)

        self.grif = ImageTk.PhotoImage(Image.open(
            path + 'гриф.png'))
        self.grif_canv = tk.Canvas(
            width=WIDTH+200, height=HEIGHT/1.4, bg='white')
        self.grif_canv.pack(side=tk.TOP)
        self.grif_canv.create_image(20, 3, image=self.grif, anchor=tk.NW)

        self.qvart = ImageTk.PhotoImage(Image.open(
            path + 'qvart.png'))
        self.qvart_canv = tk.Canvas(width=400, height=400)
        self.qvart_canv = tk.Canvas(width=400, height=400)
        self.qvart_canv.place(x=0, y=300)
        self.qvart_canv.create_image(0, 0, image=self.qvart, anchor=tk.NW)

        self.chord_monitor = tk.Canvas(width=200, height=50, bg='ivory')
        self.chord_monitor.place(x=490, y=288)
        self.chord_monitor_text = self.chord_monitor.create_text(100, 25, text='', font='Veranda 14')

        self.button_frame = tk.LabelFrame()
        self.button_frame.place(x=405, y=310)
        self.button_save_chord = tk.Button(self.button_frame, text='Save Chord', command=self.save_chord)
        self.button_save_chord.pack()

        self.chord_name_entry = tk.Entry(self.root, width=12)
        self.chord_name_entry.place(x=405, y=290)
        self.chord_place = tk.Canvas(self.root, width=50, height=30)

        self.chord_base_frame = tk.LabelFrame(text='Chord Base')
        self.chord_base_canvas = tk.Canvas(self.chord_base_frame, width = 827, height=517, bg="ivory")
        self.chord_base_frame.place(x=700, y=282, width = 827, height=460)
        self.chord_base_canvas.pack()
        self.chord_name_listbox = tk.Listbox(self.chord_base_frame)
        self.chord_name_listbox.place(x=10, y=10, width=144, height = 420)

        
        self.chord_listbox = tk.Listbox(self.chord_base_frame)
        self.chord_listbox.place(x=180, y=10, width=610, height = 420)

        for chordlist in data:
            b = tk.Button(self.chord_name_listbox, text=f"{chordlist}",
                command=lambda chord=chordlist: fill_chord_listbox(chord))
            b.pack()        

        self.scrollbar1 = tk.Scrollbar(self.chord_base_frame)
        self.scrollbar1.place(x = 160, y = 10, height = 420)
        self.scrollbar2 = tk.Scrollbar(self.chord_base_frame)
        self.scrollbar2.place(x = 800, y = 10, height = 420)


        def fill_chord_listbox(chordlist):
            self.chord_listbox.delete(0, tk.END)
            letter = 'a'
            column = 0
            row = 0
            for chord in sorted(data[chordlist])[::]:
                if not chord or (chord[0] < "A" or chord[0] > "Z"):
                    continue
                if not chord.startswith(letter):
                    row += 1
                    column = 0
                    letter = chord[0]
                b = tk.Button(self.chord_listbox, text=f"{chord}",
                command=lambda name=chord: self.show_chord(data[chordlist][name], name))
                b.grid(row=row, column=column, sticky=tk.W)
                column += 1




        def callback(event): 
            if "entry" in str(event.widget):
                self.chord_name_entry.focus()
                return
            self.root.focus()
        self.root.bind('<Motion>', callback)

        s = 6
        self.chord_canv.create_text(150, 10*(s*1), text=f'ВСЕ АККОРДЫ:')
        self.chord_canv.create_text(150, 10*(s*2), text=f'ТОНИКА:')
        self.chord_canv.create_text(150, 10*(s*3), text=f'СУБ-ДОМИНАНТА:')
        self.chord_canv.create_text(150, 10*(s*4), text=f'ДОМИНАНТА:')

        self.chord_name = 0
        self.tonal = None

        self.field = [["-", "-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-"],
        ["-", "-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-"],
        ["-", "-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-"],
        ["-", "-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-"],
        ["-", "-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-"],
        ["-", "-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-"]]

        self.chord = copy.deepcopy(self.field)
    
    def show_chord(self, chord, name):

        self.chord = copy.deepcopy(chord)
        self.field = copy.deepcopy(chord)

        for j in range(len(self.field)):
            for i in range(len(self.field[j])):
                if self.field[j][i] != "-":
                    self.field[j][i] = '0' + self.field[j][i]
        self.tonal = "All"
        print(self.field)
        self.draw_field()
        self.print_now_chord()

    def draw_field(self):

        self.grif_canv.delete(tk.ALL)
        self.grif_canv.create_image(20, 3, image=self.grif, anchor=tk.NW)

        for y in range(len(self.field)):
            for x in range(len(self.field[0])):

                note = self.field[y][x]

                coord_y = Y_ES[y]
                coord_x = X_ES[x]

                if note == '-':
                    continue

                if note.startswith('+'):
                    self.draw_dot(coord_x, coord_y, note[1:], 'red')

                elif note.startswith('0'):
                    self.draw_dot(coord_x, coord_y, note[1:], 'pink')

                elif note in TONALS_NOTES[self.tonal]:
                    self.draw_dot(coord_x, coord_y, note)


    def give_name(self):
        self.chord_name = self.chord_name_entry.get()
    
    def set_chord_default(self):
        self.chord = [["-", "-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-"],
            ["-", "-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-"],
            ["-", "-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-"],
            ["-", "-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-"],
            ["-", "-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-"],
            ["-", "-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-"]]

    def save_chord(self):
        self.give_name()
        if self.chord_name != 0:
            save_chords_data(self.chord_name, self.chord)
            # self.set_chord_default()
            self.chord_name = 0


    def define_click(self, x, y):
        # for i in self.chord:
        #     print(i)
        # print()
        for i in self.field:
            print(i)
        print()
        print()

        x = min(X_ES, key=lambda a:abs(a-x))
        y = min(Y_ES, key=lambda a:abs(a-y))
        x_num = X_ES_NUM[x]
        y_num = Y_ES_NUM[y]
        note_show = self.field[y_num][x_num]

        if self.field[y_num][x_num] == '-':
            self.field[y_num][x_num] = '0' + grif_field[y_num][x_num]
            self.chord[y_num][x_num] = grif_field[y_num][x_num]

        elif note_show.startswith('0'):
            self.field[y_num][x_num] = '-'
            self.chord[y_num][x_num] = '-'

        else:
            if note_show.startswith('+'):
                note_show = note_show[1:]
                self.chord[y_num][x_num] = '-'
                self.field[y_num][x_num] = note_show
            elif note_show in TONALS_NOTES[self.tonal]:
                self.field[y_num][x_num] = '+' + note_show
                self.chord[y_num][x_num] = note_show

        for i in self.chord:
            print(i)
        print()
        print()

        self.draw_field()
        self.print_now_chord()

    def print_now_chord(self):

        self.chord_monitor.delete(tk.ALL)
        for chord_name, chord in data['All chords'].items():
            if self.chord == chord:
                self.chord_monitor_text = self.chord_monitor.create_text(100, 25, text=f'{chord_name}', font='Veranda 14')
                return
        self.chord_monitor_text = self.chord_monitor.create_text(100, 25, text='Аккорда нет в базе', font='Veranda 14')


    def draw_dot(self, x, y, note_show, color='white'):
        self.grif_canv.create_oval(x-15.5, y-15.5, x+15.5, y+15.5, fill=color, outline='black')
        self.grif_canv.create_text(x, y, text=note_show, font='Veranda 15')


    def draw_info(self, tonal):
        
        self.field = [["-", "-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-"],
        ["-", "-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-"],
        ["-", "-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-"],
        ["-", "-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-"],
        ["-", "-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-"],
        ["-", "-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-" ,"-"]]

        self.chord = copy.deepcopy(self.field)

        grif_field_copy = copy.deepcopy(grif_field)
        # drawing qvart
        self.draw_circle(self.tonal)

        #полностью чистим гриф and paint again
        self.grif_canv.delete(tk.ALL)
        #adding grif picture
        self.grif_canv.create_image(20, 3, image=self.grif, anchor=tk.NW)

        try:
            self.chord_canv.delete(self.chords)
            self.chord_canv.delete(self.chords1)
            self.chord_canv.delete(self.chords2)
            self.chord_canv.delete(self.chords3)
            self.chord_canv.delete(self.chords4)
        except:
            pass

        tonal_chords = []

#"""getting chords

        if self.tonal.endswith('m'):
            for i in range(len(TONALS_NOTES[self.tonal])):
                if i + 1 in (1, 4, 5):
                    tonal_chords.append(TONALS_NOTES[self.tonal][i]+'m')
                else:
                    tonal_chords.append(TONALS_NOTES[self.tonal][i])
            dominant = tonal_chords[4][:-1]
        else:
            dominant = None
            for i in range(len(TONALS_NOTES[self.tonal])):
                if i + 1 not in (1, 4, 5):
                    tonal_chords.append(TONALS_NOTES[self.tonal][i]+'m')
                else:
                    tonal_chords.append(TONALS_NOTES[self.tonal][i])
#drawing chords"""
            TEXT_X = 150
            s = 6
        self.chords = self.chord_canv.create_text(
            TEXT_X, 10*(s*0.6), justify=tk.LEFT, text=f'{", ".join(tonal_chords)}', font='Veranda 17', fill="red")
        self.chords1 = self.chord_canv.create_text(
            TEXT_X, 10*(s*1.6), justify=tk.LEFT, text=f'{tonal_chords[0]}', font='Veranda 17', fill="red")
        self.chords2 = self.chord_canv.create_text(
            TEXT_X, 10*(s*2.6), justify=tk.LEFT, text=f'{tonal_chords[3]}', font='Veranda 17', fill="red")
        self.chords3 = self.chord_canv.create_text(
            TEXT_X, 10*(s*3.6), justify=tk.LEFT, text=f'{tonal_chords[4]}, {dominant}', font='Veranda 17', fill="red")


        for string in grif_field_copy:
            for note in string:
                if note in TONALS_NOTES[self.tonal]:
                    note_index = string.index(note)
                    str_index = grif_field_copy.index(string)
                    note_show = note

                    self.field[str_index][note_index] = note_show
                    grif_field_copy[str_index][note_index] = '-'

        self.draw_field()


    def draw_circle(self, tonal):
        self.qvart_canv.delete(tk.ALL)
        self.qvart = ImageTk.PhotoImage(Image.open(
            path + 'circles\\' + CIRCLES[self.tonal]))
        self.qvart_canv.create_image(0, 0, image=self.qvart, anchor=tk.NW)

def main():
    window = Window()

    def detect_click_qvart(event):
        x, y = event.x, event.y
        
        for rect in RECT_FOR_BUTTONS:
            if x > RECT_FOR_BUTTONS[rect][0][0] and\
               x < RECT_FOR_BUTTONS[rect][0][1] and\
               y > RECT_FOR_BUTTONS[rect][1][0] and\
               y < RECT_FOR_BUTTONS[rect][1][1]:
               window.tonal = rect
               window.draw_info(window.tonal)
               
    
    def detect_click_grif(event):
        x,y = event.x, event.y
        window.define_click(x, y)

    window.grif_canv.bind('<Button-1>', detect_click_grif)
    window.qvart_canv.bind('<Button-1>', detect_click_qvart)


    window.root.mainloop()


if __name__ == "__main__":
    main()

