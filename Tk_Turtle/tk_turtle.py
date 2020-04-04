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