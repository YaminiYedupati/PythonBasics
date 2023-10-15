import math

class Circle:
    name = "Circle" #class variable
    def __init__(self, radius):
        self.radius = radius #instance variable

    #Imp: self is like this in other languages. It holds the current state of the class for us.
    def calculate_area(self):
        return round(math.pi * self.radius ** 2, 2)
        

circle_1 = Circle(42)
print("Area of circle with radius", circle_1.radius, "is", circle_1.calculate_area())

circle_1.radius = 7
print("Area of circle with radius", 7, "is", Circle(7).calculate_area())

print(Circle.name) #class variables can be accessed using class name

#print(Circle.radius) #does not work - instance variables can only be accessed through instances
