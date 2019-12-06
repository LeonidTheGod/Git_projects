import tkinter as tk
from settings import *
from random import choice, randint
import copy


class Rectangle:
    def __init__(self, field):

        zero_in_game = 0
        for i in range(FIELD_SIZE):
            if 0 in field.field[i]:
                zero_in_game = 1
                break

        if zero_in_game:
            while True:
                y = randint(0, FIELD_SIZE - 1)
                if 0 in field.field[y]:
                    x = randint(0, FIELD_SIZE - 1)
                    if field.field[y][x] == 0:
                        break

        self.rect = field.game_canvas.create_rectangle(4 + (x)*RECT_SIZE, 4 + (y)*RECT_SIZE, 4 + (x)*RECT_SIZE + RECT_SIZE,
                                                       4 + (y)*RECT_SIZE + RECT_SIZE, fill=IVORY)
        self.text = field.game_canvas.create_text(4 + (x)*RECT_SIZE  + RECT_SIZE/2, 4 + (y)*RECT_SIZE + RECT_SIZE/2 ,text = '2')

        field.text_field[y][x] = self.text
        field.field[y][x] = 2
        field.rect_field[y][x] = self.rect

    def define_key(self, event):
        global field
        if event.keysym == 'd' or event.keysym == 'Right':
            self.move_rect(field, 'd')
        elif event.keysym == 'a' or event.keysym == 'Left':
            self.move_rect(field, 'a')
        elif event.keysym == 's' or event.keysym == 'Down':
            self.move_rect(field, 's')
        elif event.keysym == 'w' or event.keysym == 'Up':
            self.move_rect(field, 'w')

    def move_rect(self, field, side):

        if side == 'd':
            for y in range(FIELD_SIZE):
                for x in range(FIELD_SIZE - 1, -1, -1):
                    i = 1
                    while x + 1 < FIELD_SIZE and field.field[y][x] != 0:

                        if field.field[y][x + 1] == field.field[y][x] and i > 0:
                            field.field[y][x + 1] = field.field[y][x + 1] * 2
                            field.field[y][x] = 0

                            field.game_canvas.delete(field.text_field[y][x],field.text_field[y][x + 1])
                            field.game_canvas.delete(field.rect_field[y][x],field.rect_field[y][x + 1])
                            field.text_field[y][x] = 0
                            field.rect_field[y][x] = 0
                            field.rect_field[y][x + 1] = \
                                field.game_canvas.create_rectangle(
                                    4 + (x+1)*RECT_SIZE, 4 + (y) *
                                RECT_SIZE, 4 + (x+1)*RECT_SIZE + RECT_SIZE,
                                    4 + (y)*RECT_SIZE + RECT_SIZE, fill=COLORS[field.field[y][x + 1]])

                            field.text_field[y][x + 1] = \
                                field.game_canvas.create_text(
                                        4 + (x+1)*RECT_SIZE + RECT_SIZE / 2, 4 + (y) *
                                    RECT_SIZE + RECT_SIZE / 2, text = str(field.field[y][x + 1]))

                            i -= 1

                        else:
                            if field.field[y][x + 1] == 0:
                                field.game_canvas.move(
                                    field.rect_field[y][x], RECT_SIZE, 0)
                                field.game_canvas.move(
                                    field.text_field[y][x], RECT_SIZE, 0)
                                field.field[y][x], field.field[y][x +
                                                                  1] = field.field[y][x + 1], field.field[y][x]
                                field.rect_field[y][x], field.rect_field[y][x +
                                                                            1] = field.rect_field[y][x + 1], field.rect_field[y][x]
                                field.text_field[y][x], field.text_field[y][x + 1] = field.text_field[y][x + 1], field.text_field[y][x]


                        x += 1
        if side == 'a':
            for y in range(FIELD_SIZE):
                for x in range(FIELD_SIZE):
                    l = 1

                    while x - 1 >= 0 and field.field[y][x] != 0:

                        if field.field[y][x - 1] == field.field[y][x] and l > 0:

                            field.field[y][x - 1] = field.field[y][x - 1] * 2
                            field.field[y][x] = 0

                            field.game_canvas.delete(field.text_field[y][x],field.text_field[y][x - 1])
                            field.game_canvas.delete(field.rect_field[y][x])
                            field.game_canvas.delete(field.rect_field[y][x - 1])

                            field.text_field[y][x] = 0
                            field.rect_field[y][x] = 0

                            field.rect_field[y][x - 1] = \
                                field.game_canvas.create_rectangle(
                                    4 + (x-1)*RECT_SIZE, 4 + (y) *
                                RECT_SIZE, 4 + (x-1)*RECT_SIZE + RECT_SIZE,
                                    4 + (y)*RECT_SIZE + RECT_SIZE, fill=COLORS[field.field[y][x - 1]]
                            )
                            field.text_field[y][x - 1] = \
                                field.game_canvas.create_text(
                                        4 + (x-1)*RECT_SIZE + RECT_SIZE / 2, 4 + (y) *
                                    RECT_SIZE + RECT_SIZE / 2, text = str(field.field[y][x - 1]))
                            l -= 1

                        else:
                            if field.field[y][x - 1] == 0:
                                field.game_canvas.move(
                                    field.rect_field[y][x], -RECT_SIZE, 0)                                
                                field.game_canvas.move(
                                    field.text_field[y][x], -RECT_SIZE, 0)

                                field.field[y][x], field.field[y][x - 1] = field.field[y][x - 1], field.field[y][x]
                                field.rect_field[y][x], field.rect_field[y][x -
                                                                            1] = field.rect_field[y][x - 1], field.rect_field[y][x]
                                field.text_field[y][x], field.text_field[y][x - 1] = field.text_field[y][x - 1], field.text_field[y][x]
                        x -= 1
        if side == 'w':
            print('up')
            for x in range(FIELD_SIZE):
                for y in range(FIELD_SIZE):
                    m = 1
                    while y - 1 >= 0 and field.field[y][x] != 0:
                        if field.field[y - 1][x] == field.field[y][x] and m > 0:

                            field.field[y - 1][x] = field.field[y - 1][x] * 2
                            field.field[y][x] = 0

                            field.game_canvas.delete(field.text_field[y][x],field.text_field[y - 1][x])
                            field.game_canvas.delete(field.rect_field[y][x])
                            field.game_canvas.delete(
                                field.rect_field[y - 1][x])

                            field.text_field[y][x] = 0
                            field.rect_field[y][x] = 0
                            field.rect_field[y - 1][x] = \
                                field.game_canvas.create_rectangle(
                                    4 + (x)*RECT_SIZE, 4 + (y-1) *
                                RECT_SIZE, 4 + (x)*RECT_SIZE + RECT_SIZE,
                                    4 + (y-1)*RECT_SIZE + RECT_SIZE, fill=COLORS[field.field[y - 1][x]])
                            field.text_field[y - 1][x] = \
                                field.game_canvas.create_text(
                                    4 + (x)*RECT_SIZE + RECT_SIZE / 2, 4 + (y - 1) *
                                RECT_SIZE + RECT_SIZE / 2, text = str(field.field[y-1][x]))
                            m -= 1
                        else:
                            if field.field[y - 1][x] == 0:
                                field.game_canvas.move(
                                    field.text_field[y][x], 0, -RECT_SIZE)
                                field.game_canvas.move(
                                    field.rect_field[y][x], 0, -RECT_SIZE )
                                field.field[y][x], field.field[y -
                                                               1][x] = field.field[y - 1][x], field.field[y][x]
                                field.rect_field[y][x], field.rect_field[y -
                                                                         1][x] = field.rect_field[y - 1][x], field.rect_field[y][x]
                                field.text_field[y][x], field.text_field[y - 1][x] = field.text_field[y - 1][x], field.text_field[y][x]

                        y -= 1
        if side == 's':
            for x in range(FIELD_SIZE):
                for y in range(FIELD_SIZE, -1, -1):
                    n = 1

                    while y + 1 < FIELD_SIZE and field.field[y][x] != 0:
                        if field.field[y + 1][x] == field.field[y][x] and n > 0:

                            field.field[y + 1][x] = field.field[y + 1][x] * 2
                            field.game_canvas.delete(field.text_field[y][x],field.text_field[y + 1][x])
                            field.game_canvas.delete(field.rect_field[y][x])
                            field.game_canvas.delete(
                                field.rect_field[y + 1][x])

                            field.rect_field[y][x] = 0
                            field.text_field[y][x] = 0
                            field.field[y][x] = 0

                            field.rect_field[y + 1][x] = field.game_canvas.create_rectangle(
                                4 + (x)*RECT_SIZE, 4 + (y+1) *
                                RECT_SIZE, 4 + (x)*RECT_SIZE + RECT_SIZE,
                                4 + (y+1)*RECT_SIZE + RECT_SIZE, fill=COLORS[field.field[y + 1][x]])
                            field.text_field[y + 1][x] = \
                                field.game_canvas.create_text(
                                    4 + (x)*RECT_SIZE + RECT_SIZE / 2, 4 + (y + 1) *
                                RECT_SIZE + RECT_SIZE / 2, text = str(field.field[y+1][x]))
                            n -= 1
                        else:
                            if field.field[y + 1][x] == 0:
                                field.game_canvas.move(
                                    field.rect_field[y][x], 0, RECT_SIZE)
                                field.game_canvas.move(
                                    field.text_field[y][x], 0, RECT_SIZE)
                                field.field[y][x], field.field[y +
                                                               1][x] = field.field[y + 1][x], field.field[y][x]
                                field.rect_field[y][x], field.rect_field[y +
                                                                         1][x] = field.rect_field[y + 1][x], field.rect_field[y][x]
                                field.text_field[y][x], field.text_field[y + 1][x] = field.text_field[y + 1][x], field.text_field[y][x]
                                
                        y += 1
        Rectangle(field)
        for i in field.text_field:
            print(i)


class Window:
    def __init__(self, root):
        self.game_frame = tk.LabelFrame()
        self.game_canvas = tk.Canvas(self.game_frame, width=WINDOW_WIDTH,
                                     height=WINDOW_WIDTH, bg=IVORY)
        self.game_frame.pack()
        self.game_canvas.pack()
        self.field = [[0 for i in range(FIELD_SIZE)]
                      for i in range(FIELD_SIZE)]
        self.text_field = copy.deepcopy(self.field)
        self.rect_field = [[0 for i in range(FIELD_SIZE)]
                           for i in range(FIELD_SIZE)]
        self.coordin_grid = [[BORDER_WIDTH + 1 + RECT_SIZE * i,
                              BORDER_WIDTH + 1 - 0.1 + RECT_SIZE + i * RECT_SIZE]
                             for i in range(FIELD_SIZE)]

    def create_border(self):
        self.game_canvas.create_rectangle(
            3, 3, WINDOW_WIDTH, WINDOW_WIDTH, width=BORDER_WIDTH)

    def restart(self):
        pass

    def undo(self):
        pass

    def change_size(self):
        pass


def main():
    global field
    root = tk.Tk()
    root.geometry(ROOT_GEOMETRY)
    field = Window(root)
    field.create_border()

    for i in range(3):
        rect = Rectangle(field)

    root.bind('<Key>', rect.define_key)

    root.mainloop()


if __name__ == "__main__":
    main()
