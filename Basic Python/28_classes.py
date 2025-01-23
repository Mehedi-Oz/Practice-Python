class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")

Point1 = Point()
Point1.draw()
Point1.x=100
print(Point1.x)