class Circle():
    def __init__(self, r):
        self.radius = r

    def circle_area(self):
       return self.radius ** 2

newcircle = Circle(7)
    
print("Dimension of circle -radius  %d" % (newcircle.radius))
print("Area of circle :", newcircle.circle_area())