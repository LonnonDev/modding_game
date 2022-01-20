class Color:
    def __init__(r, g, b):
       self.r = r
       self.g = g
       self.b = b 

class Rectangle:
    def __init__(x: float, y: float, width: float, height: float, color: Color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color 
