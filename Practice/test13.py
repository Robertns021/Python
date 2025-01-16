class Point:
    #constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def move(self):
        print("Move")
    

    def draw(self):
        print("Draw")

    

point1 = Point(10, 20)
point1.draw()