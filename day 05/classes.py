#Capital P (Pascal naming)
class Point:
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")


point1 = Point()
#after writting .  we should have our defs
point1.draw()
# If you need a larger class, should be like "EmailClient"

point1.x = 10
point1.y = 20

print(point1.x)

#This is completelly different than the other.
point2 = Point()
#If now we do point2.x we will have an AttributeError
#We have to define it again
point2.x = 1
print(point2.x)