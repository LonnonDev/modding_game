class Color:
    def __init__(r: int, g: int, b: int):
       self.r = r
       self.g = g
       self.b = b 

class Vector:
    def __init__(x: float, y: float, z: float = 0.0):
        self.x = x
        self.y = y
        self.z = z

class Trangle: 
    def __init__(v1, v2, v3, color):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3
        self.color = color