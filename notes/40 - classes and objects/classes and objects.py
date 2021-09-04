class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, xIn=0, yIn=0):
        """ Create a new point at x, y """
        self.x = xIn
        self.y = yIn
        
    def __str__(self):
        return f"({self.x}, {self.y})"

    def distanceFromOrigin(self):
        """ Compute my distance from the origin """
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5
# Other statements outside the class continue below here.
#END OF THE CLASS POINT

class Rectangle:
    """ A class to manufacture rectangle objects """

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h """
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)
        

a = Point()
print(f'{a}')
b = Point(4,5)
print(f'{b}')

box = Rectangle(Point(0, 0), 100, 200)