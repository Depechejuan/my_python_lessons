class Point:
    # This is use to create (or construct) an object
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def move(self):
        print("Move")


    def draw(self):
        print("Draw")


# point = Point()
# print(point.x)
# this will generate an error like this:
# AttributeError: 'Point' object has no attribute 'x'

point = Point(10, 20)
print(point.x)
point.x = 11